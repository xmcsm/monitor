"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/groups/',views.group_list),
    path('api/groups/<int:pk>',views.group_detail),
    path('api/apps/',views.app_list),
    path('api/app/<int:pk>',views.app_detail),
    path('api/hosts/', views.host_list),
    path('api/host/<int:pk>', views.host_detail),
    path('api/history/', views.app_history_list),
    path('api/statistics/', views.app_statistics_list),
    path('api/managerapp/<int:pk>', views.manager_detail),
    path('api/statistics/<int:pk>', views.app_statistics_list),
    path('api/count/groups/', views.count_groups_statistics_detail),
    path('api/count/group/<int:pk>', views.count_group_statistics_detail),
    path('api-auth/',include('rest_framework.urls'))
]
