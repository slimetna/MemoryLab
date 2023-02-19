from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from MemoryLab import settings
from MemoryLabStore.views import index, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/<str:slug>', product_detail, name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
