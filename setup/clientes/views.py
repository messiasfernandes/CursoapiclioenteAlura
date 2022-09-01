from rest_framework import viewsets
from clientes.serializer import ClientesSerializer
from clientes.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class= ClientesSerializer
