from django.db import migrations


EARLY_IPHONES = [
    "iPhone (2007)",
    "iPhone 3G",
    "iPhone 3GS",
    "iPhone 4",
    "iPhone 4S",
    "iPhone 5",
    "iPhone 5c",
    "iPhone 5s",
    "iPhone SE (2016)",
]


def add_early_iphones(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Brand = apps.get_model("ads", "Brand")
    Model = apps.get_model("ads", "Model")

    category, _ = Category.objects.get_or_create(name="Телефоны")
    brand, _ = Brand.objects.get_or_create(name="Apple", category=category)

    for model_name in EARLY_IPHONES:
        Model.objects.get_or_create(name=model_name, brand=brand)


def remove_early_iphones(apps, schema_editor):
    Model = apps.get_model("ads", "Model")
    Model.objects.filter(name__in=EARLY_IPHONES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0027_add_iphone17"),
    ]

    operations = [
        migrations.RunPython(add_early_iphones, remove_early_iphones),
    ]
