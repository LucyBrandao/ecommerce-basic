from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('list', ProductListView.as_view(), name='product-list'),
]
