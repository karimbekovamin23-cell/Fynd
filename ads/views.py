from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, JsonResponse
from django.utils import timezone
from django.db.models import Q, Avg, Sum, Case, When, BooleanField
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from datetime import timedelta
import hashlib
import uuid
import json
import requests

from .models import Ad, Profile, Review, Favorite, Chat, Message, Payment, Category, Brand, Model
from .forms import AdForm


def unread_messages(user):
    return Message.objects.filter(
        is_read=False
    ).exclude(sender=user).filter(
        chat__buyer=user
    ).count() + Message.objects.filter(
        is_read=False
    ).exclude(sender=user).filter(
        chat__seller=user
    ).count()


def ad_list(request):
    Ad.objects.filter(
        promoted_until__lt=timezone.now()
    ).update(
        promotion_level=0,
        is_promoted=False
    )

    query = request.GET.get('q') or ''
    city = request.GET.get('city')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    sort = request.GET.get('sort')

    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    model_id = request.GET.get('model')

    year = request.GET.get('year')
    mileage = request.GET.get('mileage')
    transmission = request.GET.get('transmission')
    engine = request.GET.get('engine')
    drive = request.GET.get('drive')
    power = request.GET.get('power')
    wheel = request.GET.get('wheel')
    color = request.GET.get('color')
    memory = request.GET.get('memory')
    color_phone = request.GET.get('color_phone')

    ads = Ad.objects.filter(is_published=True).annotate(
        is_active_promo=Case(
            When(promoted_until__gt=timezone.now(), then=True),
            default=False,
            output_field=BooleanField()
        )
    )

    if category_id:
        ads = ads.filter(category_id=category_id)
    if brand_id:
        ads = ads.filter(brand_id=brand_id)
    if model_id:
        ads = ads.filter(model_id=model_id)
    if year:
        ads = ads.filter(year=year)
    if mileage:
        ads = ads.filter(mileage__lte=mileage)
    if transmission:
        ads = ads.filter(transmission=transmission)
    if engine:
        ads = ads.filter(engine=engine)
    if drive:
        ads = ads.filter(drive=drive)
    if power:
        ads = ads.filter(power=power)
    if wheel:
        ads = ads.filter(wheel=wheel)
    if color:
        ads = ads.filter(color__icontains=color)
    if memory:
        ads = ads.filter(memory=memory)
    if color_phone:
        ads = ads.filter(color__icontains=color_phone)
    if query:
        ads = ads.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(city__icontains=query)
        )
    if city:
        ads = ads.filter(city__icontains=city)
    if price_min:
        ads = ads.filter(price__gte=price_min)
    if price_max:
        ads = ads.filter(price__lte=price_max)

    if sort == "cheap":
        ads = ads.order_by("-promotion_level", "-promoted_at", "price")
    elif sort == "expensive":
        ads = ads.order_by("-promotion_level", "-promoted_at", "-price")
    elif sort == "popular":
        ads = ads.order_by("-promotion_level", "-promoted_at", "-views")
    else:
        ads = ads.order_by("-promotion_level", "-promoted_at", "-created_at")

    unread = 0
    if request.user.is_authenticated:
        unread = unread_messages(request.user)

    categories = Category.objects.all()
    brands = Brand.objects.filter(category_id=category_id) if category_id else Brand.objects.none()
    models = Model.objects.filter(brand_id=brand_id) if brand_id else Model.objects.none()

    paginator = Paginator(ads, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "ads/ad_list.html", {
        "ads": page_obj,
        "page_obj": page_obj,
        "query": query,
        "city": city,
        "price_min": price_min,
        "price_max": price_max,
        "sort": sort,
        "category": category_id,
        "brand": brand_id,
        "model": model_id,
        "categories": categories,
        "brands": brands,
        "models": models,
        "unread": unread,
        "show_navbar": False,
    })


@login_required
def add_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.is_published = False
            ad.expires_at = timezone.now() + timedelta(days=30)
            ad.save()
            messages.success(request, 'Объявление отправлено на модерацию 🚀')
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/add_ad.html', {'form': form})


def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    if request.user != ad.author:
        ad.views += 1
        ad.save()

    seller = ad.author
    reviews = Review.objects.filter(target=seller)
    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg']
    review_count = reviews.count()

    price_min = ad.price * 0.7
    price_max = ad.price * 1.3

    similar_ads = Ad.objects.filter(
        category=ad.category,
        price__gte=price_min,
        price__lte=price_max
    ).exclude(pk=ad.pk)

    if ad.brand:
        similar_ads = similar_ads.filter(brand=ad.brand)
    if ad.city:
        similar_ads = similar_ads.filter(city__icontains=ad.city)
    if similar_ads.count() < 4:
        similar_ads = Ad.objects.filter(category=ad.category).exclude(pk=ad.pk)
    if similar_ads.count() < 4:
        similar_ads = Ad.objects.exclude(pk=ad.pk)

    similar_ads = similar_ads.order_by("-created_at")[:8]

    return render(request, 'ads/ad_detail.html', {
        'ad': ad,
        'seller': seller,
        'avg_rating': avg_rating,
        'review_count': review_count,
        'similar_ads': similar_ads,
    })


@login_required
def toggle_favorite(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    favorite, created = Favorite.objects.get_or_create(user=request.user, ad=ad)

    if not created:
        favorite.delete()
        ad.favorites_count = max(0, ad.favorites_count - 1)
    else:
        ad.favorites_count += 1

    ad.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    ads = Ad.objects.filter(author=user).order_by("-created_at")
    reviews = Review.objects.filter(target=user)
    total_views = ads.aggregate(total=Sum('views'))['total'] or 0
    total_favorites = ads.aggregate(total=Sum('favorites_count'))['total'] or 0

    return render(request, 'ads/profile.html', {
        'profile_user': user,
        'profile': profile,
        'ads': ads,
        'reviews': reviews,
        'total_views': total_views,
        'total_favorites': total_favorites,
    })


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.phone = request.POST.get("phone")
        profile.telegram = request.POST.get("telegram")
        if request.FILES.get("avatar"):
            profile.avatar = request.FILES.get("avatar")
        profile.save()
        return redirect("profile", username=request.user.username)

    return render(request, "ads/edit_profile.html", {"profile": profile})


@login_required
def edit_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk, author=request.user)

    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = AdForm(instance=ad)

    return render(request, "ads/edit_ad.html", {"form": form})


@login_required
def delete_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    if ad.author != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        ad.delete()

    return redirect('profile', username=request.user.username)


@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    ads = [f.ad for f in favorites]
    return render(request, "ads/favorites.html", {"ads": ads})


@login_required
@ratelimit(key='user', rate='5/m', method='POST', block=True)
def add_review(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        rating = request.POST.get("rating")
        text = request.POST.get("text")
        Review.objects.create(
            author=request.user,
            target=user,
            rating=rating,
            text=text
        )

    return redirect("profile", username=username)


def chat(request):
    return render(request, "ads/chat.html")


@login_required
def chat_view(request, chat_id):
    chat_obj = get_object_or_404(Chat, id=chat_id)

    chat_messages = Message.objects.filter(chat=chat_obj).order_by("created_at")

    Message.objects.filter(
        chat=chat_obj,
        is_read=False
    ).exclude(sender=request.user).update(is_read=True)

    return render(request, "ads/chat_room.html", {
        "chat": chat_obj,
        "messages": chat_messages,
    })


@login_required
def chat_list(request):
    chats = (
        Chat.objects.filter(buyer=request.user) |
        Chat.objects.filter(seller=request.user)
    ).distinct()

    for chat_obj in chats:
        chat_obj.last_message = Message.objects.filter(
            chat=chat_obj
        ).order_by("-created_at").first()
        chat_obj.unread = Message.objects.filter(
            chat=chat_obj,
            is_read=False
        ).exclude(sender=request.user).count()

    return render(request, "ads/chat_list.html", {"chats": chats})


@login_required
def open_chat(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if request.user == ad.author:
        return redirect("/")

    chat_obj, _ = Chat.objects.get_or_create(
        ad=ad,
        buyer=request.user,
        seller=ad.author
    )

    return redirect("chat_view", chat_obj.id)


def unread_count(request):
    if request.user.is_anonymous:
        return JsonResponse({"count": 0})

    count = Message.objects.filter(
        chat__buyer=request.user
    ).exclude(sender=request.user).count() + Message.objects.filter(
        chat__seller=request.user
    ).exclude(sender=request.user).count()

    return JsonResponse({"count": count})


def get_brands(request):
    category_id = request.GET.get("category_id")

    if not category_id or category_id == "None":
        return JsonResponse({"brands": []})

    brands = Brand.objects.filter(category_id=int(category_id))
    data = [{"id": b.id, "name": b.name} for b in brands]
    return JsonResponse({"brands": data})


def get_models(request):
    brand_id = request.GET.get("brand_id")

    if not brand_id or brand_id == "None":
        return JsonResponse({"models": []})

    models = Model.objects.filter(brand_id=int(brand_id))
    data = [{"id": m.id, "name": m.name} for m in models]
    return JsonResponse({"models": data})


def promote_ad(request, ad_id, days):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)

    days = int(days)

    if days == 1:
        level = 1
    elif days == 3:
        level = 2
    elif days == 7:
        level = 3
    else:
        level = 1

    now = timezone.now()

    if ad.promoted_until and ad.promoted_until > now:
        ad.promoted_until += timedelta(days=days)
    else:
        ad.promoted_until = now + timedelta(days=days)
        ad.promoted_at = now

    if level > ad.promotion_level:
        ad.promotion_level = level

    ad.is_promoted = True
    ad.save()

    return redirect("profile", username=request.user.username)


def choose_promotion(request, pk):
    ad = get_object_or_404(Ad, pk=pk, author=request.user)
    return render(request, "ads/choose_promotion.html", {"ad": ad})


def buy_promotion(request, pk, days):
    ad = get_object_or_404(Ad, pk=pk, author=request.user)
    ad.is_promoted = True
    ad.promoted_until = timezone.now() + timedelta(days=int(days))
    ad.save()
    return redirect('profile', username=request.user.username)


def _generate_token(data, password):
    data_copy = data.copy()
    data_copy["Password"] = password
    data_copy.pop("Token", None)
    sorted_items = sorted(data_copy.items())
    token_string = "".join(str(v) for _, v in sorted_items)
    return hashlib.sha256(token_string.encode("utf-8")).hexdigest()


@login_required
@ratelimit(key='user', rate='10/m', method='GET', block=True)
def create_payment(request, ad_id, days):
    ad = get_object_or_404(Ad, id=ad_id, author=request.user)

    days = int(days)

    if days == 1:
        amount = 99
    elif days == 3:
        amount = 199
    elif days == 7:
        amount = 399
    else:
        amount = 99

    order_id = str(uuid.uuid4())

    payment = Payment.objects.create(
        user=request.user,
        ad=ad,
        amount=amount,
        days=days,
        status="pending",
        external_id=order_id
    )

    webhook_url = request.build_absolute_uri(reverse('payment_webhook'))

    data = {
        "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
        "Amount": amount * 100,
        "OrderId": order_id,
        "NotificationURL": webhook_url,
    }

    token_data = {
        "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
        "Amount": amount * 100,
        "OrderId": order_id,
        "NotificationURL": webhook_url,
        "Password": settings.TINKOFF_SECRET_KEY,
    }

    data["Token"] = _generate_token(token_data, settings.TINKOFF_SECRET_KEY)

    response = requests.post("https://securepay.tinkoff.ru/v2/Init", json=data)

    try:
        res = response.json()
    except Exception:
        return JsonResponse({
            "error": "not json",
            "status": response.status_code,
            "text": response.text,
        })

    if not res.get("Success"):
        return JsonResponse(res)

    return redirect(res["PaymentURL"])


@csrf_exempt
def payment_webhook(request):
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"ok": False})

    external_id = data.get("OrderId")
    status = data.get("Status")

    if status != "CONFIRMED":
        return JsonResponse({"ok": True})

    try:
        payment = Payment.objects.get(external_id=external_id)
    except Payment.DoesNotExist:
        return JsonResponse({"ok": False})

    if payment.status == "paid":
        return JsonResponse({"ok": True})

    payment.status = "paid"
    payment.save()

    ad = payment.ad
    ad.is_promoted = True

    if payment.days == 1:
        level = 1
    elif payment.days == 3:
        level = 2
    elif payment.days == 7:
        level = 3
    else:
        level = 1

    ad.promotion_level = level
    ad.promoted_at = timezone.now()
    ad.promoted_until = timezone.now() + timedelta(days=payment.days)
    ad.save()

    return JsonResponse({"ok": True})
