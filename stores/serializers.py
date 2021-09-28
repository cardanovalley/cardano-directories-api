from rest_framework import serializers
from stores.models import Store, Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ["name", "url"]


class StoreSerializer(serializers.HyperlinkedModelSerializer):
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

    def to_representation(self, instance):
        store_representation = super().to_representation(instance)

        country_name = None
        if instance.country is not None:
            country_name = instance.country.name
        store_representation["country_name"] = country_name

        return store_representation

    # def create(self, validated_data):
    #     country_data = validated_data.pop("country")
    #     store = Store.objects.create(**validated_data)
    #     store.country = country_data
    #     return store
