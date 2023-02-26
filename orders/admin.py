from django.contrib import admin
from .models import Order, OrderItem, PaymentMethod

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentMethod)