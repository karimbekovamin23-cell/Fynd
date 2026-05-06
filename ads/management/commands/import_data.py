import json
from django.core.management.base import BaseCommand
from ads.models import Category, Brand, Model


class Command(BaseCommand):
    help = "Импорт JSON"

    def handle(self, *args, **kwargs):

        with open("ads/data/data.json", encoding="utf-8") as f:
            data = json.load(f)

        for category_name, brands in data.items():

            category, _ = Category.objects.get_or_create(name=category_name)

            for brand_name, models in brands.items():

                brand, _ = Brand.objects.get_or_create(
                    name=brand_name,
                    category=category
                )

                for model_name in models:
                    Model.objects.get_or_create(
                        name=model_name,
                        brand=brand
                    )

        print("🔥 ГОТОВО")