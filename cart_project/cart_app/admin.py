from django.contrib import admin
from .models import Customer, SKU, CartDetail
# Register your models here.
admin.site.register(Customer)
admin.site.register(SKU)
admin.site.register(CartDetail)
