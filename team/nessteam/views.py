
from django.contrib.auth import get_user_model
User = get_user_model()
from nessteam.serializers import UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()
