from django.test import TestCase
from django.core.management import call_command

from stores.models import Store


class CreateStoreTestCase(TestCase):
    def test_create_store(self):
        """Test that a particular store from the json file
        was correctly created with the import_stores command."""

        call_command("import_stores", "stores.json")

        store_queryset = Store.objects.filter(name="Activity Tours")

        self.assertEqual(store_queryset.first().name, "Activity Tours")
        self.assertEqual(store_queryset.count(), 1)

    def test_no_duplicate_stores(self):
        """Tests that no duplciate stores are created after calling
        the import_stores command again"""

        call_command("import_stores", "stores.json")

        store_queryset_before_command = Store.objects.all()

        call_command("import_stores", "stores.json")

        store_queryset_after_command = Store.objects.all()

        self.assertEqual(
            store_queryset_after_command.count(), store_queryset_before_command.count()
        )


class UpdateStoreTestCase(TestCase):
    def setUp(self):

        store1 = Store.objects.create(
            name="modified Activity Tours",
            picture="assets/images/explore/activity-tours.png",
            googlemaps_link="https://goo.gl/maps/QJ3hZi5yk4ZnreWv7",
            website="https://www.activity-tours.com/",
            address="Filolaou 124, Athens",
        )

    def test_store1_updated(self):
        """First the creation of the store is tested and then
        the import_stores command is called and the update of
        the store is checked."""
        store1_name = "modified Activity Tours"
        store_query = Store.objects.filter(website="https://www.activity-tours.com/")
        self.assertEqual(store_query.first().name, store1_name)

        call_command("import_stores", "stores.json")
        store1_name = "Activity Tours"
        store_query = Store.objects.filter(website="https://www.activity-tours.com/")
        self.assertEqual(store_query.first().name, store1_name)
