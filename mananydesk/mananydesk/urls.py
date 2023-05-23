"""mananydesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from main import views as mainv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainv.home,name='home'),
    path('new/',mainv.ClientAddView.as_view(),name='new'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('update/<int:pk>/',mainv.ClientUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',mainv.ClientDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>/',mainv.ClientDetailView.as_view(),name='detail'),
    path('import/',mainv.DataImport.as_view(),name='import'),
    path('imp/',mainv.Import,name='imp'),
    path('list_imp/',mainv.FilesList,name='liste_import'),
]
