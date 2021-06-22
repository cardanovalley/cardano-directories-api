from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Store(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    address = models.CharField(max_length=200)
    googlemaps = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
