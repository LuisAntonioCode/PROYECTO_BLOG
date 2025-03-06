from rest_framework import routers
from .views import CategoryApiViewSet

router_Category = routers.DefaultRouter()
router_Category.register(r'categories', CategoryApiViewSet, 'categorias')
urlpatterns = router_Category.urls