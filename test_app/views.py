from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet
from test_app.models import Employee
from test_app.serializers import EmployeeSerializer

class EmployeeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,\
                      mixins.ListModelMixin, GenericViewSet):
    queryset = Employee.objects.filter(active=True)
    # permission_classes = []
    serializer_class = EmployeeSerializer

router = DefaultRouter()
router.register("employee", EmployeeViewset, basename="employee")