# views.py
from rest_framework import viewsets
from .models import Roles, Users
from .serializers import RolesSerializer, UsersSerializer

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
