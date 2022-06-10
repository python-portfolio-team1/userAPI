from pyexpat import model
from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.modelserializer):
    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'birthday', 'phone', 'address', 'password']
