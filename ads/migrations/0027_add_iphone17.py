from django.db import migrations


def add_iphone17(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Brand = apps.get_model("ads", "Brand")
    Model = apps.get_model("ads", "Model")

    category, _ = Category.objects.get_or_create(name="Телефоны")
    brand, _ = Brand.objects.get_or_create(name="Apple", category=category)

    for model_name in ["iPhone 17", "iPhone 17 Air", "iPhone 17 Pro", "iPhone 17 Pro Max"]:
        Model.objects.get_or_create(name=model_name, brand=brand)


def remove_iphone17(apps, schema_editor):
    Model = apps.get_model("ads", "Model")
    Model.objects.filter(name__in=["iPhone 17", "iPhone 17 Air", "iPhone 17 Pro", "iPhone 17 Pro Max"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0026_seed_categories_full"),
    ]

    operations = [
        migrations.RunPython(add_iphone17, remove_iphone17),
    ]
