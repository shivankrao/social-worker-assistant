from rest_framework import routers
from .views import MainViewSet

router = routers.DefaultRouter()
router.register('main', MainViewSet, 'main')
# router.register(URL PREFIX, VIEWSET CLASS, URL NAME)

urlpatterns = router.urls