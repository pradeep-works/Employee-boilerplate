from rest_framework import serializers
from users.models import User, Group

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(BaseSerializer):
    class Meta:
        model = Group
        fields = BaseSerializer.Meta.fields + ['name']