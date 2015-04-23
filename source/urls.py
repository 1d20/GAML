from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from apps.core.api import SingerViewSet, SongViewSet, SongInfoViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'singers', SingerViewSet)
router.register(r'songs', SongViewSet)
router.register(r'songinfos', SongInfoViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'^$', 'apps.core.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
