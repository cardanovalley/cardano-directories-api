import os, json

from django.conf import settings
from django.core.management.base import BaseCommand
from stores.models import Store, Country


class Command(BaseCommand):
    help = "Adds a list of stores from a JSON file to database."

    def add_arguments(self, parser):
        default_stores_json_path = settings.BASE_DIR
        parser.add_argument("json_file_name", help="Name of json file")
        parser.add_argument(
            "--file_path", default=default_stores_json_path, help="json file path"
        )

    def handle(self, *args, **options):

        with open(os.path.join(options["file_path"], options["json_file_name"])) as f:
            data = json.load(f)

            store_created_count = 0

            for store in data:
                name = store["name"]
                picture = store["picture"]
                address = store["address"]
                googlemaps_link = store["googlemaps_link"]
                website = store["website"]
                country = Country.objects.filter(name=store["country"]).first()

                obj, created = Store.objects.update_or_create(
                    # name=name,
                    # picture=picture,
                    address=address,
                    # googlemaps_link=googlemaps_link,
                    website=website,
                    defaults={
                        "name": name,
                        "picture": picture,
                        "googlemaps_link": googlemaps_link,
                        "country": country,
                    },
                )

                if created:
                    store_created_count += 1

                if obj is None:
                    self.stdout.write(self.style.ERROR(f"{name} was not created."))

        self.stdout.write(
            self.style.SUCCESS(f"{store_created_count} stores were created.")
        )
