from datetime import datetime

from rest_framework import serializers

from .models import Libro


class LibroGenericSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=200)
    autor = serializers.CharField(max_length=100)
    anio_publicacion = serializers.IntegerField()

    def create(self, validated_data):
        return Libro.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get("titulo", instance.titulo)
        instance.autor = validated_data.get("autor", instance.autor)
        instance.anio_publicacion = validated_data.get(
            "anio_publicacion", instance.anio_publicacion
        )
        instance.save()
        return instance


class LibroSerializer(serializers.ModelSerializer):
    edad_libro = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ["id", "titulo", "autor", "anio_publicacion", "edad_libro"]
        # O usar fields = '__all__' para todos los campos

    def get_edad_libro(self, obj):
        return datetime.now().year - obj.anio_publicacion

    def validate_anio_publicacion(self, value):
        if value > 2025:
            raise serializers.ValidationError(
                "El año de publicación no puede ser futuro"
            )
        return value

    def validate(self, data):
        if len(data["titulo"]) < 3:
            raise serializers.ValidationError(
                "El título debe tener al menos 3 caracteres"
            )
        return data
