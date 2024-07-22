from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include, re_path
from userapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^user$', views.userAPI),
    re_path(r'^user/(?P<id>\d+)$', views.userAPI),
    re_path(r'^user/(?P<id>\d+)/update$', views.userAPI),
    re_path(r'^user/(?P<id>\d+)/delete$', views.userAPI),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


