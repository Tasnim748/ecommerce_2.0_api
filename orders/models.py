from django.db import models
from products.models import Product, Customer

# Create your models here.

class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.customer.name + "_" + str(self.id)

    @property
    def date(self):
        return self.date_ordered.date()

    @property
    def net_quantity(self):
        quant = sum([item.quantity for item in self.orderitem_set.all()])
        return quant

    @property
    def net_price(self):
        price = sum([item.price for item in self.orderitem_set.all()])
        return price

    @property
    def paymentMethod(self):
        return self.payment.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=False, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.order) + "_" + str(self.product)

    @property
    def price(self):
        return self.product.price * self.quantity

