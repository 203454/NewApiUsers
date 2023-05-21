from .models import Usuario
from rest_framework import viewsets, permissions, filters
from .serializer import UsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
