from django.contrib.gis.db import models as models


class ServiceTag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    location = models.PointField(geography=True)

    class Meta:
        ordering = ('name',)


class Service(models.Model):
    service_tag = models.ForeignKey(
        to=ServiceTag,
        on_delete=models.CASCADE,
        related_name='services'
    )
    service_provider = models.ForeignKey(
        to=ServiceProvider,
        on_delete=models.CASCADE,
        related_name='services'
    )
    description = models.TextField()
    approved = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
