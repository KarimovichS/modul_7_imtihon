from rest_framework.serializers import ModelSerializer
from .models import UserPasswordManager


class UserPasswordManagerSerializer(ModelSerializer):
    class Meta:
        model = UserPasswordManager
        fields = '__all__'
