from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, ListModelMixin
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated

from users.models import User, Group
from users.serializers import UserSerializer, GroupSerializer
from users.permission import IsAdminOnly
# Create your views here.

class UserViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, \
                  UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, \
                   UpdateModelMixin, GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOnly]

router = DefaultRouter()
router.register("users", UserViewset, "users")
router.register("groups", GroupViewset, "groups")