from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    @property
    def name(self):
        return self.user.username
    
    @property
    def email(self):
        if self.user.email:
            return self.user.email
        else:
            return "noEmail"

    def __str__(self):
        if self.user.email:
            return self.email
        else:
            return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    categoryKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "_id_" + str(self.id)

    @property
    def imageUrl(self):
        if self.photo:
            return self.photo.url
        else:
            return None

    @property
    def category(self):
        return self.categoryKey.name


class Review(models.Model):
    comment = models.CharField(max_length=500)
    star = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    commenter = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment + " (" + str(self.star) + ")"

    @property
    def commenterName(self):
        return self.commenter.name

    @property
    def productName(self):
        return self.product.name

