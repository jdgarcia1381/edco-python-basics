from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Libro
from .serializers import LibroSerializer


# Create your views here.
class LibroAPIView(APIView):
    def get(self, request):
        return Response("Hello World Libros", status=status.HTTP_200_OK)


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
