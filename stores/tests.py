from django.test import TestCase
from stores.models import Store

# from stores.management.commands.import_stores import Command
from django.core.management import call_command


class ImportStoresCommandTestCase(TestCase):
    def setUp(self):
        Store.objects.create(
            name="lion",
            website="ww.jfre.com",
            picture="jie/edm/",
            address="dertu 25",
            googlemaps="map.link/place/cool",
        )
        storelion = Store()
        storelion.name = "lion"
        storelion.save()

    def test_creates_store(self):
        """Test that it creates the stores from json file"""
        args = []
        opts = {}
        stores_query = Store.objects.filter(
            name="activity tours"
        )  # Should return stores_query = []

        self.assertEqual(stores_query.count(), 0)

        call_command("import_stores", *args, **opts)

        stores_query = Store.objects.filter(name="activity tours")

        self.assertEqual(stores_query.first().name, "activity tours")
        self.assertEqual(stores_query.count(), 1)
