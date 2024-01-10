from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductPriceViewSet


router = DefaultRouter()

router.register('products', ProductViewSet, 'product' )
router.register('product-prices', ProductPriceViewSet, 'prices')
