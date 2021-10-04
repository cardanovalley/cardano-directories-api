from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Store(models.Model):
    name = models.CharField(max_length=150)

    picture = models.ImageField(
        max_length=200, upload_to="stores/", blank=True, null=True
    )
    address = models.CharField(max_length=200)
    googlemaps_link = models.CharField(
        max_length=200, blank=True
    )  # Link to googlemap position
    website = models.CharField(max_length=200)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.website.startswith(("http://", "https://")):
            self.website = "https://" + self.website
        super().save(force_insert, force_update, using, update_fields)
