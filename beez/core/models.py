from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.urls import reverse


class Apiary(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='apiaries', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
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
        return reverse('apiary-detail', args=[self.pk])


class Hive(models.Model):
    apiary = models.ForeignKey(Apiary, related_name='hives', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    terminated = models.BooleanField(default=False)
    date_terminated = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hive-detail', args=[self.pk])

    @property
    def last_recorded_weight(self):
        inspection = self.inspections.filter(weight__isnull=False).first()

        if inspection:
            return inspection.weight


class Inspection(models.Model):
    hive = models.ForeignKey(Hive, related_name='inspections', on_delete=models.CASCADE)
    date = models.DateTimeField()
    weight = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0)])
    saw_queen = models.BooleanField(default=False)
    # TODO: Add a whole bunch of parameters
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Inspection on {}'.format(self.date)

    def get_absolute_url(self):
        return reverse('inspection-detail', args=[self.pk])


class Harvest(models.Model):
    hive = models.ForeignKey(Hive, related_name='harvests', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(validators=[validators.MinValueValidator(0)])

    def __str__(self):
        return 'Harvest on {} ({} kg)'.format(self.date, self.weight)