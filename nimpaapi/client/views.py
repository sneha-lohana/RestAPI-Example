from rest_framework import viewsets
from api.serializers import ClientSerializer
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serialzer_class = ClientSerializer(queryset)
