"""matlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from matlab import urlsapp
from django.http import HttpResponse
from app.views import HomeViews
from admin import urls as adminUrls



#这里是总的url入口，如果想路由到其他地方，那么需要在这里分路由
urlpatterns = [
    path('',HomeViews.welcome),
    path('admin/<str:module>/<str:method>',adminUrls.adminindex),
    path('matlab', include(urlsapp.urlpatterns))#路由后面不要加/
]




