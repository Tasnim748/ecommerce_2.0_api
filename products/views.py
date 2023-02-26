from .models import Product, Review
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializer, ProdDetailSerializer, ReviewSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# the token claim and customization
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(request):
    print(request.user)
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prodDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProdDetailSerializer(product, many=False)

    reviews = product.review_set.all()
    reviewSerializer = ReviewSerializer(reviews, many=True)

    data = serializer.data
    # data["reviews"] = reviewSerializer.data
    print(data, reviewSerializer.data)
    return Response(data)

@api_view(['POST'])
def reviewCreate(request, pk):
    product = Product.objects.get(id=pk)
    customer = request.user.customer

    data = request.data
    try:
        Review.objects.create(product=product, commenter=customer, comment=data["comment"], star=data["star"])
        return Response("success")
    except:
        return Response("failed! invalid data")


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        data = request.data
        username = data['username']
        password = data['password']
        print(data)
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response('user creation successful')
        except Exception as e:
            return Response(str(e))
    return Response('Not allowed other than post request')
    
    

