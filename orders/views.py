from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrders(request):
    user = request.user
    customer = user.customer
    orders = customer.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response('no order found')
