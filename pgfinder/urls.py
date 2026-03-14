from django.contrib import admin
from django.urls import path
from listings import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)