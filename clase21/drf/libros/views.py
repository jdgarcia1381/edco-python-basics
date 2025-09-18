from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Libro
from .serializers import LibroSerializer


# Create your views here.
class LibroListView(APIView):
    # permission_classes = []

    def get(self, request):
        libros = Libro.objects.all()
        data = []
        for libro in libros:
            data.append(
                {
                    "id": libro.id,
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "anio_publicacion": libro.anio_publicacion,
                }
            )
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        titulo = request.data.get("titulo")
        autor = request.data.get("autor")
        anio_publicacion = request.data.get("autor")
        if titulo and autor and anio_publicacion:
            libro = Libro.objects.create(
                titulo=titulo, autor=autor, anio_publicacion=anio_publicacion
            )
            return Response(
                {
                    "id": libro.id,
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "anio_publicacion": libro.anio_publicacion,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST
        )


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        """Filtrar libros por año si se especifica"""
        queryset = Libro.objects.all()
        # http://localhost:8000/api/libros/?anio=2000
        anio = self.request.query_params.get("anio")
        if anio is not None:
            queryset = queryset.filter(anio_publicacion=anio)
        return queryset

    def perform_create(self, serializer):
        """Personalizar la creación"""
        serializer.save()
