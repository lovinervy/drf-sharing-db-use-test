from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Product, ProductPrice

class ProductPriceSerializer(ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    last_price = SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_current_price(self, instance: Product):
        last_price = instance.prices.all().order_by('-date').first()
        if last_price is None:
            return None
        return ProductPriceSerializer(last_price).data


class ProductViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = ProductSerializer
    queryset = Product.objects.all().prefetch_related('prices')


class ProductPriceViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    pagination_class = None
    serializer_class = ProductPriceSerializer
    queryset = ProductPrice.objects.all()
