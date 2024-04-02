from django.contrib.sitemaps import Sitemap
from .models import Book


class BookSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.created_at
