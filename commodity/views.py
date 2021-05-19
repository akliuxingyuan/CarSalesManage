# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Category, Factory, Car, CustomerTrade, FactoryTrade
from .serializer import CategorySerializer, FactorySerializer, CustomerTradeSerializer, FactoryTradeSerializer


class MyPageNumberPagination(PageNumberPagination):
    """
    自定义分页
    """
    page_size = 20  # 默认每页大小
    max_page_size = 100  # 前端最多每页大小
    page_query_param = 'page'  # 前端查询关键字，指定第几页
    page_size_query_param = 'page_size'  # 前端查询关键字，指定每页大小


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination
    filter_fields = ['cat_id', 'cat_name', 'cat_pid', 'cat_level']
    filter_backends = [OrderingFilter]
    ordering_fields = ['cat_id', 'cat_name', 'cat_pid', 'cat_level']


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination
    filter_fields = ['cid', 'cname', 'cprice', 'number']
    filter_backends = [OrderingFilter]
    ordering_fields = ['cid', 'cname', 'cprice', 'number']


class CustomerTradeViewSet(ModelViewSet):
    queryset = CustomerTrade.objects.all()
    serializer_class = CustomerTradeSerializer
    pagination_class = MyPageNumberPagination
    filter_fields = ['ctid', 'cid']
    filter_backends = [OrderingFilter]
    ordering_fields = ['ctid', 'ctprice', 'cid']


class FactoryTradeViewSet(ModelViewSet):
    queryset = FactoryTrade.objects.all()
    serializer_class = FactoryTradeSerializer
    pagination_class = MyPageNumberPagination
    filter_fields = ['ftid', 'fid']
    filter_backends = [OrderingFilter]
    ordering_fields = ['ftid', 'ftprice', 'fid']
