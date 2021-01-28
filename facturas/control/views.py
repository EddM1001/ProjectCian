from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Factura
from .serializes import ClienteSerializer, FacturaSerializer, LoginSerializer, UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken 

# A continuacion se crearan las vistas.

class ClienteViewSet(viewsets.ModelViewSet):
    #se deterina que se pueda visualizar solo si se esta registrado
    #tanto para clientes como para facturas
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    

#creacion de la clase para el login
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })


class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

#Encargado del registro
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class ResultadoDos(generics.ListAPIView):
    serializer_class = FacturaSerializer
    def get_queryset(self):
        return Factura.objects.values('watts')

#obtener la suma del costo por cliente
#costo = 
#Factura.objects.all()
# .aggregate(
# costo = Sum('tarifa')
# )


#obtener promedio de watts consumidos por cliente
#promedio = Factura.objects
#.values('cliente')
#.annotate(
#  facturas = Count('cliente'),
#  promedioWatts = Avg('watts')
#)
#.order_by('cliente')