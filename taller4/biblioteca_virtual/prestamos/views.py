from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Prestamo
from .serializers import PrestamoListSerializer, PrestamoSerializer


# Create your views here.
class PrestamoAPIView(APIView):
    def get(self, request):
        return Response("Hello World Préstamos", status=status.HTTP_200_OK)


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PrestamoListSerializer
        return super().get_serializer_class()

    # def perform_create(self, serializer):
    #     serializer.usuario = self.request.user
    #     serializer.save()
