from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from ecommerce.product.views import hello_world


urlpatterns = [
    path('', hello_world, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('product/', include('ecommerce.product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
