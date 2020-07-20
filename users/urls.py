"""Defines url patterns for users."""

from django.urls import path, include
from django.contrib.auth.views import LoginView#导入类
from django.contrib.auth import logout
from . import views
# 修改模板路径

app_name = 'users'
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登录界面
    path('login/', LoginView.as_view(),name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register/',views.register,name='register')
]
#path('login/',LoginView.as_view(template_name='users/login.html'),name='login')
