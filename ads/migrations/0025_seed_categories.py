from django.db import migrations

DATA = {
    "Авто": {
        "BMW": ["1 Series","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X5","X6","X7","M2","M3","M4","M5","Z4"],
        "Mercedes-Benz": ["A-Class","C-Class","E-Class","S-Class","GLA","GLB","GLC","GLE","GLS","G-Class"],
        "Audi": ["A3","A4","A5","A6","A7","A8","Q3","Q5","Q7","Q8","TT","R8"],
        "Toyota": ["Corolla","Camry","RAV4","Land Cruiser","Land Cruiser Prado","Highlander","Prius","Yaris"],
        "Volkswagen": ["Golf","Passat","Polo","Tiguan","Touareg","Jetta"],
        "Hyundai": ["Elantra","Sonata","Tucson","Santa Fe","Creta","i30","Solaris"],
        "Kia": ["Rio","Ceed","K5","Sportage","Sorento","Picanto","Stinger"],
        "Honda": ["Civic","Accord","CR-V","HR-V","Pilot"],
        "Nissan": ["Almera","Qashqai","X-Trail","Patrol","Teana","GT-R"],
        "Mazda": ["Mazda 3","Mazda 6","CX-3","CX-5","CX-9","MX-5"],
        "Lada": ["Vesta","Granta","Niva","Largus","XRAY"],
        "Renault": ["Logan","Sandero","Duster","Kaptur","Arkana","Megane"],
        "Skoda": ["Octavia","Superb","Kodiaq","Karoq","Rapid","Fabia"],
        "Mitsubishi": ["Outlander","Pajero","L200","Eclipse Cross","ASX"],
        "Subaru": ["Forester","Outback","Impreza","Legacy","XV","WRX"],
        "Lexus": ["RX","LX","NX","GX","IS","ES","LS"],
        "Porsche": ["911","Cayenne","Macan","Panamera","Taycan"],
        "Volvo": ["XC60","XC90","S60","S90","V60","V90"],
        "Ford": ["Focus","Mondeo","Explorer","Mustang","Kuga","F-150"],
        "Chevrolet": ["Cruze","Captiva","Tahoe","Camaro","Trailblazer"],
    },
    "Телефоны": {
        "Apple": ["iPhone 8","iPhone X","iPhone XR","iPhone XS","iPhone 11","iPhone 12","iPhone 13","iPhone 14","iPhone 15","iPhone 16","iPhone SE"],
        "Samsung": ["Galaxy S21","Galaxy S22","Galaxy S23","Galaxy S24","Galaxy A52","Galaxy A53","Galaxy A54","Galaxy Note 20","Galaxy Z Fold"],
        "Xiaomi": ["Redmi Note 10","Redmi Note 11","Redmi Note 12","Redmi Note 13","Mi 11","Mi 12","Mi 13","POCO X5","POCO F5"],
        "Huawei": ["P30","P40","P50","Mate 30","Mate 40","Mate 50","Nova 9","Nova 10"],
        "Honor": ["20","30","50","70","90","Magic 5","Magic 6"],
        "OnePlus": ["9","9 Pro","10 Pro","11","Nord 2","Nord 3"],
        "Google": ["Pixel 5","Pixel 6","Pixel 6a","Pixel 7","Pixel 8","Pixel 8 Pro"],
        "Realme": ["9 Pro","10 Pro","GT 2","GT Neo","C55"],
        "Nokia": ["G21","G42","C32","X30"],
    },
    "Ноутбуки": {
        "Apple": ["MacBook Air M1","MacBook Air M2","MacBook Air M3","MacBook Pro 14","MacBook Pro 16"],
        "Dell": ["XPS 13","XPS 15","Inspiron 15","Alienware M15"],
        "HP": ["Pavilion","Envy","Omen","ProBook","EliteBook"],
        "Lenovo": ["ThinkPad X1","ThinkPad T14","IdeaPad 5","Legion 5","Yoga"],
        "Asus": ["ZenBook","VivoBook","ROG Strix","TUF Gaming"],
        "Acer": ["Aspire 5","Swift 3","Nitro 5","Predator Helios"],
        "MSI": ["GF63","Katana","Stealth 15M","Creator"],
    },
    "Одежда": {
        "Nike": ["Air Max","Air Force 1","Dunk","Tech Fleece","Jordan"],
        "Adidas": ["Ultraboost","NMD","Superstar","Gazelle","Yeezy"],
        "Puma": ["RS-X","Suede","Future Rider"],
        "Zara": ["Куртки","Пальто","Футболки","Джинсы","Платья"],
        "H&M": ["Футболки","Худи","Джинсы","Куртки"],
        "Uniqlo": ["Ultra Light Down","AIRism","Heattech"],
        "Gucci": ["Сумки","Кроссовки","Одежда"],
        "Louis Vuitton": ["Сумки","Аксессуары","Обувь"],
    },
    "Недвижимость": {
        "Квартиры": ["Студия","1-комнатная","2-комнатная","3-комнатная","4+ комнатная"],
        "Дома": ["Коттедж","Таунхаус","Дача","Частный дом"],
        "Коммерческая": ["Офис","Склад","Магазин","Производство"],
        "Земля": ["ИЖС","СНТ","Сельхозназначение"],
    },
    "Запчасти": {
        "Двигатель": ["Контрактный","Новый","Б/у"],
        "Подвеска": ["Амортизаторы","Пружины","Рычаги","Ступицы"],
        "Кузов": ["Капот","Бампер","Двери","Крылья","Стёкла"],
        "Электрика": ["Фары","Генератор","Стартер","Аккумулятор"],
        "Тормоза": ["Диски","Колодки","Суппорты"],
        "Шины и диски": ["Летние","Зимние","Всесезонные","Диски"],
    },
    "Услуги": {
        "Ремонт техники": ["Телефоны","Ноутбуки","Телевизоры","Планшеты"],
        "Ремонт авто": ["Кузовной","Двигатель","Электрика","Шиномонтаж"],
        "Ремонт квартир": ["Косметический","Капитальный","Сантехника"],
        "Красота": ["Маникюр","Парикмахер","Массаж","Татуаж"],
        "IT услуги": ["Создание сайтов","Дизайн","SEO","Программирование"],
        "Обучение": ["Репетитор","Курсы","Онлайн-обучение"],
    },
    "Другое": {
        "Разное": ["Б/у","Новое"],
        "Антиквариат": ["Монеты","Картины","Мебель"],
        "Спорт": ["Велосипеды","Тренажёры","Туризм"],
        "Детские товары": ["Коляски","Игрушки","Одежда"],
        "Животные": ["Собаки","Кошки","Птицы","Рыбы"],
    },
}


def seed_categories(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Brand = apps.get_model("ads", "Brand")
    Model = apps.get_model("ads", "Model")

    for category_name, brands in DATA.items():
        category, _ = Category.objects.get_or_create(name=category_name)
        for brand_name, models in brands.items():
            brand, _ = Brand.objects.get_or_create(name=brand_name, category=category)
            for model_name in models:
                Model.objects.get_or_create(name=model_name, brand=brand)


def unseed_categories(apps, schema_editor):
    Category = apps.get_model("ads", "Category")
    Category.objects.filter(name__in=DATA.keys()).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0024_add_ad_indexes"),
    ]

    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]
