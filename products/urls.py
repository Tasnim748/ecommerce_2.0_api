from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('create-review/<str:pk>/', views.reviewCreate, name='review-create'),
    path('<str:pk>/', views.prodDetail, name='product-detail' ),
]