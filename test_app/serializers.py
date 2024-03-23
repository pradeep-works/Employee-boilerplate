from test_app.models import Employee
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from rest_framework import status

class BaseSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class EmployeeSerializer(BaseSerializer):
    class Meta:
        model = Employee
        fields = BaseSerializer.Meta.fields + ['name', 'id_number', 'date_of_joining', 'salary', 'active']

    # Validation during processing a request
    def validate(self, attrs):
        salary = attrs.get('salary', None)
        # Salary should not be less than 20000
        if salary and salary < 20000:
            raise ValidationError(detail="Salary should not be less than 20000", code=status.HTTP_400_BAD_REQUEST)
        return super().validate(attrs)
    
    # Logic should be implemented only during creating a record
    def create(self, validated_data):
        return super().create(validated_data)
    
    # Logic should be implemented only during updating a record
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
