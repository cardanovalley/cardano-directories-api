import os, json

from django.conf import settings
from django.core.management.base import BaseCommand
from stores.models import Store


class Command(BaseCommand):
    help = "Adds a list of stores from a JSON file to database."

    def handle(self, *args, **options):

        stores_json_path = settings.BASE_DIR

        with open(os.path.join(stores_json_path, "stores.json")) as f:
            data = json.load(f)

            store_count = 0

            for store in data:
                name = store["name"]
                picture = store["picture"]
                address = store["address"]
                googlemaps = store["googlemaps"]
                website = store["website"]

                obj, created = Store.objects.get_or_create(
                    name=name,
                    picture=picture,
                    address=address,
                    googlemaps=googlemaps,
                    website=website,
                )

                if created:
                    store_count += 1

                if obj is None:
                    self.stdout.write(self.style.ERROR(f"{name} was not created."))

        self.stdout.write(self.style.SUCCESS(f"{store_count} stores were created."))
