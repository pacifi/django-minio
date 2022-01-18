from rest_framework import routers

from myapp.views import PersonaViewSet

router = routers.SimpleRouter()
router.register(r'personas', PersonaViewSet)

urlpatterns = router.urls
