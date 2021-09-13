from rest_framework import serializers
from stores.models import Store, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer(required=False, read_only=True)

    class Meta:
        model = Store
        fields = [
            "name",
            "website",
            "address",
            "googlemaps_link",
            "picture",
            "country",
        ]
