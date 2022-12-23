from .serializers import *
from products.models import *
from users.models import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Productserializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['^title']
    ordering_fields = ['id', 'title']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]


class Order_detailViewSet(viewsets.ModelViewSet):
    queryset = Order_detail.objects.all()
    serializer_class = Order_detailSerializer
    authentication_classes = [JWTAuthentication]