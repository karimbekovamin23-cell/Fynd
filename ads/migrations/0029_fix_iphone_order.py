from django.db import migrations

IPHONES_ORDERED = [
    "iPhone 3G",
    "iPhone 3GS",
    "iPhone 4",
    "iPhone 4S",
    "iPhone 5",
    "iPhone 5c",
    "iPhone 5s",
    "iPhone SE (2016)",
    "iPhone 6",
    "iPhone 6 Plus",
    "iPhone 6s",
    "iPhone 6s Plus",
    "iPhone 7",
    "iPhone 7 Plus",
    "iPhone 8",
    "iPhone 8 Plus",
    "iPhone X",
    "iPhone XR",
    "iPhone XS",
    "iPhone XS Max",
    "iPhone 11",
    "iPhone 11 Pro",
    "iPhone 11 Pro Max",
    "iPhone 12 mini",
    "iPhone 12",
    "iPhone 12 Pro",
    "iPhone 12 Pro Max",
    "iPhone 13 mini",
    "iPhone 13",
    "iPhone 13 Pro",
    "iPhone 13 Pro Max",
    "iPhone SE (2020)",
    "iPhone 14",
    "iPhone 14 Plus",
    "iPhone 14 Pro",
    "iPhone 14 Pro Max",
    "iPhone 15",
    "iPhone 15 Plus",
    "iPhone 15 Pro",
    "iPhone 15 Pro Max",
    "iPhone SE (2022)",
    "iPhone 16",
    "iPhone 16 Plus",
    "iPhone 16 Pro",
    "iPhone 16 Pro Max",
    "iPhone SE (2024)",
    "iPhone 17",
    "iPhone 17 Air",
    "iPhone 17 Pro",
    "iPhone 17 Pro Max",
]


def fix_iphone_order(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Brand = apps.get_model("ads", "Brand")
    Model = apps.get_model("ads", "Model")

    category, _ = Category.objects.get_or_create(name="Телефоны")
    brand, _ = Brand.objects.get_or_create(name="Apple", category=category)

    # удаляем все старые записи Apple в Телефонах
    Model.objects.filter(brand=brand).delete()

    # вставляем в правильном порядке
    for name in IPHONES_ORDERED:
        Model.objects.create(name=name, brand=brand)


def reverse_fix(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0028_add_early_iphones"),
    ]

    operations = [
        migrations.RunPython(fix_iphone_order, reverse_fix),
    ]
