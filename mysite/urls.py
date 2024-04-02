from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_title = 'FreeLibrary'
admin.site.site_header = "Администрирование FreeLibrary"
SOCIAL_AUTH_URL_NAMESPACE = 'social'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("polls.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("__debug__/", include("debug_toolbar.urls")),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
