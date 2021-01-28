from rest_framework import routers
from django.urls import include, path
from .views import ResultadoDos
from .views import ClienteViewSet, FacturaViewSet, LoginAPI, UserAPI, RegisterAPI

router =routers.DefaultRouter()
router.register(r'Cliente', ClienteViewSet)
router.register(r'Factura', FacturaViewSet)
#se definen las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('login', LoginAPI.as_view()),
    path('user', UserAPI.as_view()),
    path('register', RegisterAPI.as_view()),
    path('resultadodos',ResultadoDos.as_view()),
]