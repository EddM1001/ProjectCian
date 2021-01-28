from rest_framework import serializers
from .models import Cliente,Factura
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#Se crean los serializers con los metadatos correpondientes
#uno por cada modelo
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombre', 'correo', 'direccion',]

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id','cliente', 'tarifa', 'watts',]




class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user

    raise serializers.ValidationError("Credenciales incorrectas")

        
 

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    return user