import os, json

from django.core.management.base import BaseCommand
from stores.models import Country


class Command(BaseCommand):
    help = "Adds a list of countries from a JSON file to database."

    def handle(self, *args, **options):

        countries_json_path = "/home/nicky/git/ada_stores/backend/"
        with open(os.path.join(countries_json_path, "countries.json")) as f:
            data = json.load(f)

            country_count = 0

            for country in data:
                name = country["Name"]
                obj, created = Country.objects.get_or_create(name=name)

                if created:
                    country_count += 1

                if obj is None:
                    self.stdout.write(self.style.ERROR(f"{name} was not created."))

        self.stdout.write(self.style.SUCCESS(f"{country_count} countries created."))
