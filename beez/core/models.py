import pytz
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

UNITS_METRIC = 'metric'
UNITS_IMPERIAL = 'imperial'

unit_choices = [
    (UNITS_METRIC, 'Metric'),
    (UNITS_IMPERIAL, 'Imperial'),
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
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, validators=[
        validators.MinValueValidator(-90),
        validators.MaxValueValidator(90),
    ])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, validators=[
        validators.MinValueValidator(-180),
        validators.MaxValueValidator(180),
    ])
    address = models.CharField(max_length=255, blank=True, null=True)
    radius = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, default=3.0, validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(10),
    ])
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Apiaries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontend:apiary-detail', args=[self.pk])


class Hive(models.Model):
    apiary = models.ForeignKey(Apiary, related_name='hives', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    terminated = models.BooleanField(default=False)
    date_terminated = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    makes_honey = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontend:hive-detail', args=[self.pk])

    @property
    def last_recorded_weight(self):
        inspection = self.inspections.filter(weight__isnull=False).first()

        if inspection:
            return inspection.weight


class Inspection(models.Model):
    hive = models.ForeignKey(Hive, related_name='inspections', on_delete=models.CASCADE)
    date = models.DateTimeField()
    weight = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0)])
    saw_queen = models.NullBooleanField(choices=((True, 'Yes'), (False, 'No')))
    saw_eggs = models.NullBooleanField(choices=((True, 'Yes'), (False, 'No')))
    needs_food = models.NullBooleanField(choices=((True, 'Yes'), (False, 'No')))
    gave_food = models.CharField(blank=True, null=True, max_length=255)
    how_much_food = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0.1)])
    mites_counted = models.PositiveSmallIntegerField(blank=True, null=True)
    mite_treatment = models.CharField(max_length=255, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Inspection on {}'.format(self.date)

    def get_absolute_url(self):
        return reverse('frontend:inspection-detail', args=[self.pk])

    @property
    def estimated_mite_population(self):
        return self.mites_counted * 200


class Harvest(models.Model):
    hive = models.ForeignKey(Hive, related_name='harvests', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(validators=[validators.MinValueValidator(0)])

    def __str__(self):
        return 'Harvest on {} ({} {})'.format(
            self.date,
            self.weight,
            self.hive.apiary.owner.settings.current_weight_unit
        )


class Settings(models.Model):
    unit_choices = [
        ('metric', 'Metric'),
        ('imperial', 'Imperial'),
    ]
    user = models.OneToOneField(get_user_model(), related_name='settings', on_delete=models.CASCADE)
    weight_unit = models.CharField(choices=unit_choices, default=UNITS_METRIC, max_length=10)
    temperature_unit = models.CharField(choices=unit_choices, default=UNITS_METRIC, max_length=10)
    timezone = models.CharField(choices=timezone_choices, default='UTC', max_length=40)

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return 'Settings for {}'.format(self.user)

    @property
    def current_weight_unit(self):
        return unit_map[self.weight_unit]['weight']

    def current_temp_unit(self):
        return unit_map[self.temperature_unit]['temp']


class File(models.Model):
    file = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    apiary = models.ForeignKey(Apiary, null=True, blank=True, related_name='files', on_delete=models.CASCADE)
    hive = models.ForeignKey(Hive, null=True, blank=True, related_name='files', on_delete=models.CASCADE)

    def clean(self):
        if self.apiary and self.hive:
            raise ValidationError('File cannot have both an apiary and a hive')

    def __str__(self):
        if self.apiary:
            return 'Apiary file for {} ({})'.format(self.apiary, self.apiary.pk)

        if self.hive:
            return 'Hive file for {} ({})'.format(self.hive, self.hive.pk)
