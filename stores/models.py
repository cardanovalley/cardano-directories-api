from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Store(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField(max_length=200, upload_to="media/")
    address = models.CharField(max_length=200)
    googlemaps_link = models.CharField(max_length=200)  # Link to googlemap position
    website = models.CharField(max_length=200)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
