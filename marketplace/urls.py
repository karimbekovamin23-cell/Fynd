from django.contrib import admin
from django.urls import path, include
from ads import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from ads.sitemap import AdSitemap



urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.ad_list, name='ad_list'),

    path("accounts/", include("allauth.urls")),
    path('accounts/', include('django.contrib.auth.urls')),

    path('add/', views.add_ad, name='add_ad'),

    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('ad/<int:pk>/edit/', views.edit_ad, name='edit_ad'),
    path('ad/<int:pk>/delete/', views.delete_ad, name='delete_ad'),
    path('ad/<int:pk>/promote/', views.promote_ad, name='promote_ad'),
    path('ad/<int:pk>/promote/choose/', views.choose_promotion, name='choose_promotion'),
    path('ad/<int:pk>/promote/<int:days>/', views.buy_promotion, name='buy_promotion'),

    path('favorites/', views.favorites, name='favorites'),
    path('favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),

    path("review/<str:username>/", views.add_review, name="add_review"),

    # профиль
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

    # ЧАТЫ
    path("chats/", views.chat_list, name="chat_list"),
    path("chat/<int:chat_id>/", views.chat_view, name="chat_view"),
    path("chat/ad/<int:ad_id>/", views.open_chat, name="open_chat"),

    path("api/unread-count/", views.unread_count),
    path("api/chat/<int:chat_id>/messages/", views.api_chat_messages),
    
    path("api/brands/", views.get_brands),
    path("api/models/", views.get_models),
    
    path('pay/<int:ad_id>/<int:days>/', views.create_payment, name='create_payment'),
    path('payment/webhook/', views.payment_webhook),
    path('telegram/webhook/<str:secret>/', views.telegram_webhook),

    path('sitemap.xml', sitemap, {'sitemaps': {'ads': AdSitemap()}}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/\nDisallow: /accounts/\nSitemap: https://fynd-production.up.railway.app/sitemap.xml", content_type="text/plain")),
]


# 👇 ВАЖНО: НЕ ПЕРЕЗАПИСЫВАЕМ, А ДОБАВЛЯЕМ
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)