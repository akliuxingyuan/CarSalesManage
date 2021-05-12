# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import User, Role, Right
from .serializers import UserSerializer, RoleSerializer, RightSerializer


class MyPageNumberPagination(PageNumberPagination):
    """
    自定义分页
    """
    page_size = 20  # 默认每页大小
    max_page_size = 100  # 前端最多每页大小
    page_query_param = 'page'  # 前端查询关键字，指定第几页
    page_size_query_param = 'page_size'  # 前端查询关键字，指定每页大小


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPageNumberPagination
    filter_fields = ['username', 'mobile']
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'rid', 'username', 'mobile']


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ['roleName', 'roleDesc']
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'roleName']


class RightViewSet(ModelViewSet):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    filter_fields = ['authName', 'authDesc']
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'authName']
