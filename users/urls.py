from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    # path('users/', views.UserViewSet.as_view({'get': 'list'})),
    # path(r'^users/(?P<pk>\d+)/$', views.UserViewSet.as_view({'get': 'retrieve'}))
    # JWT login
    re_path(r'^login/$', obtain_jwt_token)
]

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'rights', views.RightViewSet)

urlpatterns += router.urls
