from django.contrib import admin
from .models import Category, Product, Stock, StockLog


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockLog)
