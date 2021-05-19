from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = []

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'factories', views.FactoryViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'customer_orders', views.CustomerTradeViewSet)
router.register(r'factory_orders', views.FactoryTradeViewSet)

urlpatterns += router.urls
