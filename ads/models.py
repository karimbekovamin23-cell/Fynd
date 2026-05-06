from django.db import models
from django.contrib.auth.models import User


# 👤 ПРОФИЛЬ
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.user.username


# 📂 КАТЕГОРИИ
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 🏷 БРЕНД
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="brands")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name} → {self.name}"


# 📦 МОДЕЛЬ
class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} → {self.name}"


from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):

    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    city = models.CharField(max_length=100)

    # 🚀 ПРОДВИЖЕНИЕ
    is_promoted = models.BooleanField(default=False)
    promotion_level = models.IntegerField(default=0)  # 0 = нет, 1/2/3 = уровни
    promoted_at = models.DateTimeField(null=True, blank=True)
    promoted_until = models.DateTimeField(null=True, blank=True)

    # 📂 связи
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey('Model', on_delete=models.SET_NULL, null=True, blank=True)

    # 🚗 АВТО
    year = models.IntegerField(null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    engine = models.CharField(max_length=50, blank=True, null=True)
    drive = models.CharField(max_length=50, blank=True, null=True)
    power = models.IntegerField(null=True, blank=True)
    wheel = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    # 📱 ТЕЛЕФОНЫ
    memory = models.IntegerField(null=True, blank=True)

    # 📦 остальное
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    views = models.PositiveIntegerField(default=0)
    favorites_count = models.PositiveIntegerField(default=0)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# 📸 ДОП ФОТО
class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="ads/")

    def __str__(self):
        return f"Фото {self.ad.title}"


# ❤️ ИЗБРАННОЕ
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "ad")

    def __str__(self):
        return f"{self.user} ❤️ {self.ad}"


# ⭐️ ОТЗЫВЫ
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_reviews")
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_reviews")

    rating = models.IntegerField(default=5)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} → {self.target}"


# 💬 ЧАТ
class Chat(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer_chats")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller_chats")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad.title} | {self.buyer} → {self.seller}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="chat/", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender}: {self.text[:20]}"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    amount = models.IntegerField()
    days = models.IntegerField()

    status = models.CharField(max_length=20, default="pending")

    external_id = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)