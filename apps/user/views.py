from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    """
    用户管理
    list:
        GET
        获取用户
    create:
        POST
        添加用户
    update:
        PATCH
        更新用户
    delete:
        DELETE
        删除用户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
