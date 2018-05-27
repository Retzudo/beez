from datetime import datetime

import pytz
from django.contrib.auth import get_user_model
from django.contrib.postgres.search import SearchVector
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from private_storage.fields import PrivateFileField

UNITS_METRIC = 'metric'
UNITS_IMPERIAL = 'imperial'

unit_choices = [
    (UNITS_METRIC, _('Metric')),
    (UNITS_IMPERIAL, _('Imperial')),
]

unit_map = {
    UNITS_METRIC: {
        'weight': 'kg',
        'temp': '°C'
    },
    UNITS_IMPERIAL: {
        'weight': 'lb',
        'temp': '°F'
    },
}

timezone_choices = sorted(zip(pytz.common_timezones_set, [tz.replace('_', ' ') for tz in pytz.common_timezones_set]))


class Apiary(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='apiaries', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=255)
    latitude = models.DecimalField(_('Latitude'), max_digits=9, decimal_places=6, blank=True, null=True, validators=[
        validators.MinValueValidator(-90),
        validators.MaxValueValidator(90),
    ])
    longitude = models.DecimalField(_('Longitude'), max_digits=9, decimal_places=6, blank=True, null=True, validators=[
        validators.MinValueValidator(-180),
        validators.MaxValueValidator(180),
    ])
    address = models.CharField(_('Address'), max_length=255, blank=True, null=True)
    radius = models.DecimalField(_('Radius'), max_digits=3, decimal_places=2, blank=True, null=True, default=3.0, validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(10),
    ])
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    notes = models.TextField(_('Notes'), blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Apiaries')
        ordering = ('date_created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontend:apiary-detail', args=[self.pk])

    @classmethod
    def search(cls, query):
        vector = SearchVector('name', weight='A') + \
                 SearchVector('notes', weight='B')
        return cls.objects.annotate(search=vector).filter(search=query)


class Hive(models.Model):
    apiary = models.ForeignKey(Apiary, related_name='hives', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=255)
    description = models.CharField(_('Description'), blank=True, null=True, max_length=255)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    notes = models.TextField(_('Notes'), blank=True, null=True)
    makes_honey = models.BooleanField(_('Makes honey'), default=False)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontend:hive-detail', args=[self.pk])

    @classmethod
    def search(cls, query):
        vector = SearchVector('name', weight='A') + \
                 SearchVector('description', weight='B') + \
                 SearchVector('notes', weight='C')
        return cls.objects.annotate(search=vector).filter(search=query)

    @property
    def last_recorded_weight(self):
        inspection = self.inspections.filter(weight__isnull=False).first()

        if inspection:
            return inspection.weight


class Inspection(models.Model):
    hive = models.ForeignKey(Hive, related_name='inspections', on_delete=models.CASCADE)
    date = models.DateTimeField(_('Date'))
    weight = models.FloatField(_('Weight'), blank=True, null=True, validators=[validators.MinValueValidator(0)])
    saw_queen = models.NullBooleanField(_('Saw queen'), choices=((True, 'Yes'), (False, 'No')))
    saw_eggs = models.NullBooleanField(_('Saw eggs'), choices=((True, 'Yes'), (False, 'No')))
    needs_food = models.NullBooleanField(_('Needs food'), choices=((True, 'Yes'), (False, 'No')))
    gave_food = models.CharField(_('Gave food'), blank=True, null=True, max_length=255)
    how_much_food = models.FloatField(_('How much?'), blank=True, null=True, validators=[validators.MinValueValidator(0.1)])
    mites_counted = models.PositiveSmallIntegerField(_('Mites counted'), blank=True, null=True)
    mite_treatment = models.CharField(_('Mite treatment'), max_length=255, blank=True, null=True)

    notes = models.TextField(_('Notes'), blank=True, null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return _('Inspection on {date}').format(date=self.date)

    def get_absolute_url(self):
        return reverse('frontend:inspection-detail', args=[self.pk])

    @property
    def estimated_mite_population(self):
        return self.mites_counted * 200


class Harvest(models.Model):
    hive = models.ForeignKey(Hive, related_name='harvests', on_delete=models.CASCADE)
    date = models.DateField(_('Date'))
    weight = models.FloatField(_('Weight'), validators=[validators.MinValueValidator(0)])

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return _('Harvest on {} ({} {})').format(
            self.date,
            self.weight,
            self.hive.apiary.owner.settings.current_weight_unit
        )


class Settings(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='settings', on_delete=models.CASCADE)
    weight_unit = models.CharField(_('Weight unit'), choices=unit_choices, default=UNITS_METRIC, max_length=10)
    temperature_unit = models.CharField(_('Temperature unit'), choices=unit_choices, default=UNITS_METRIC, max_length=10)
    timezone = models.CharField(_('Timezone'), choices=timezone_choices, default='UTC', max_length=40)
    language = models.CharField(_('Language'), choices=[('de', _('German')), ('en', _('English'))], default='en', max_length=4)

    class Meta:
        verbose_name_plural = _('Settings')

    def __str__(self):
        return _('Settings for {user}').format(user=self.user)

    @property
    def current_weight_unit(self):
        return unit_map[self.weight_unit]['weight']

    def current_temp_unit(self):
        return unit_map[self.temperature_unit]['temp']


class File(models.Model):
    file = PrivateFileField(_('File'), content_types='application/pdf', max_file_size=10 * 1024 * 1024)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    apiary = models.ForeignKey(Apiary, null=True, blank=True, related_name='files', on_delete=models.CASCADE)
    hive = models.ForeignKey(Hive, null=True, blank=True, related_name='files', on_delete=models.CASCADE)

    def clean(self):
        if self.apiary and self.hive:
            raise ValidationError(_('File cannot have both an apiary and a hive'))

    def __str__(self):
        if self.apiary:
            return _('Apiary file for {apiary} ({pk})').format(apiary=self.apiary, pk=self.apiary.pk)

        if self.hive:
            return _('Hive file for {hive} ({pk})').format(hive=self.hive, pk=self.hive.pk)


class Queen(models.Model):
    hive = models.OneToOneField(Hive, related_name='queen', on_delete=models.CASCADE)
    year = models.PositiveIntegerField(_('Year'), default=datetime.now().year)
    number = models.CharField(_('Number'), max_length=25)

    def get_absolute_url(self):
        return reverse('frontend:hive-detail', args=[self.hive.pk])

    @classmethod
    def search(cls, query):
        vector = SearchVector('number', weight='A')
        return cls.objects.annotate(search=vector).filter(search=query)
