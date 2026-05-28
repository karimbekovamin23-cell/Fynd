from django.contrib.sitemaps import Sitemap
from .models import Ad


class AdSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Ad.objects.filter(is_published=True).order_by('-created_at')

    def location(self, obj):
        return f"/ad/{obj.pk}/"

    def lastmod(self, obj):
        return obj.created_at
