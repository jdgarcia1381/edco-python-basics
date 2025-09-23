from libros.serializers import LibroSerializer
from rest_framework import serializers
from usuarios.serializers import CustomUserSerializer

from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


class PrestamoListSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()
    usuario = CustomUserSerializer()
    # libro = serializers.SerializerMethodField()

    class Meta:
        model = Prestamo
        fields = "__all__"

    # def get_libro(self, obj):
    #     return obj.libro.titulo
