"""demo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('mainscene/', views.mainscene),
    path('cityinfo/', views.cityinfo),
    path('showdata/', views.showdata),
    path('sigin/', views.sigin),
    path('login/', views.login),
    path('refresh/', views.refresh),
    path('show/', views.show),
]


# 北京 已经爬取180条
# 太原 已经爬取90条
# 南京 已经爬取180条
# 上海 已经爬取90条
# 沈阳 已经爬取90条
