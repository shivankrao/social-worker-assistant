from rest_framework import viewsets
from .serializers import MainSerializer
from main.models import Main

class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer