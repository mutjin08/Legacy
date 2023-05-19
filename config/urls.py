from django.contrib import admin
from django.urls import path, include

from pybo.views import base_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
