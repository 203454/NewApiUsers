from rest_framework import serializers
from .models import Usuario

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','name','last_name','username','email',)
        read_only_fields = ('created_at', )