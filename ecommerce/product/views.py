from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product


class ProductListView(ListView):

    model = Product
    


def hello_world(request):
    return render(request, 'hello_world.html')
