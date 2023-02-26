from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['date_ordered', 'paymentMethod', 'net_quantity', 'net_price', 'id', 'date']