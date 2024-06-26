from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet
from test_app.models import Employee, Department, Device
from test_app.serializers import EmployeeSerializer, DepartmentSerializer, DeviceSerializer

class EmployeeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,\
                      mixins.ListModelMixin, GenericViewSet):
    queryset = Employee.objects.filter(active=True)
    # permission_classes = []
    serializer_class = EmployeeSerializer

class DepartmentViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,\
                       mixins.ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeviceViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,\
                    mixins.ListModelMixin, GenericViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

router = DefaultRouter()
router.register("employee", EmployeeViewset, basename="employee")
router.register("department", DepartmentViewset, basename="department")
router.register("device", DeviceViewset, basename="device")
