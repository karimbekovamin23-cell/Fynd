from django import forms
from .models import Ad, Brand, Model


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad

        fields = [
            "title",
            "price",
            "description",
            "city",

            "category",
            "brand",
            "model",

            # 🚗 авто
            "year",
            "mileage",
            "transmission",
            "engine",
            "drive",
            "power",
            "wheel",
            "color",

            # 📱 телефоны
            "memory",

            "telegram",
            "image"
        ]

        widgets = {

            # 🧾 база
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: iPhone 13'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в рублях'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите товар',
                'rows': 4
            }),

            # 📂
            'category': forms.Select(attrs={'class': 'form-control'}),

            # 🏷
            'brand': forms.Select(attrs={'class': 'form-control'}),

            # 📦
            'model': forms.Select(attrs={'class': 'form-control'}),

            # 🚗 авто
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год'
            }),

            'mileage': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пробег'
            }),

            'transmission': forms.Select(attrs={'class': 'form-control'}, choices=[
                ("", "Коробка"),
                ("Автомат", "Автомат"),
                ("Механика", "Механика"),
                ("Вариатор", "Вариатор"),
                ("Робот", "Робот"),
            ]),

            'engine': forms.Select(attrs={'class': 'form-control'}, choices=[
                ("", "Двигатель"),
                ("Бензин", "Бензин"),
                ("Дизель", "Дизель"),
                ("Гибрид", "Гибрид"),
                ("Электро", "Электро"),
            ]),

            'drive': forms.Select(attrs={'class': 'form-control'}, choices=[
                ("", "Привод"),
                ("Передний", "Передний"),
                ("Задний", "Задний"),
                ("Полный", "Полный"),
            ]),

            'power': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Л.с'
            }),

            'wheel': forms.Select(attrs={'class': 'form-control'}, choices=[
                ("", "Руль"),
                ("Левый", "Левый"),
                ("Правый", "Правый"),
            ]),

            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цвет'
            }),

            # 📱
            'memory': forms.Select(attrs={'class': 'form-control'}, choices=[
                ("", "Память"),
                ("4", "4 GB"),
                ("8", "8 GB"),
                ("16", "16 GB"),
                ("32", "32 GB"),
                ("64", "64 GB"),
                ("128", "128 GB"),
                ("256", "256 GB"),
                ("512", "512 GB"),
                ("1024", "1 TB"),
                ("2048", "2 TB"),
            ]),

            # 📞
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username без @'
            }),

            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    # 🔥 ВАЖНО — ДИНАМИКА (главный фикс)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ❗ по умолчанию пусто
        self.fields['brand'].queryset = Brand.objects.none()
        self.fields['model'].queryset = Model.objects.none()

        # 📂 если выбрана категория
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['brand'].queryset = Brand.objects.filter(category_id=category_id)
            except:
                pass

        # 🏷 если выбран бренд
        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = Model.objects.filter(brand_id=brand_id)
            except:
                pass

        # 🔥 если редактирование (очень важно)
        elif self.instance.pk:
            if self.instance.brand:
                self.fields['brand'].queryset = Brand.objects.filter(category=self.instance.category)

            if self.instance.model:
                self.fields['model'].queryset = Model.objects.filter(brand=self.instance.brand)