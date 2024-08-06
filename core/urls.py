"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views import  OPER, TK, TMC, CreateOPER, CreateTK, CreateTMC, Home,  CreateCompany, CreateUser, Login, Main, TK_e, TMC_e, Users,Company,vidget,vvid
from django.urls import path

from core import views
from product.views import productApiView 
from rest_framework import routers

app_name = 'core'
router=routers.DefaultRouter()
router.register(r'api/prod',productApiView)
urlpatterns = [
    path('', vidget.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('tk/', TK.as_view(), name='tk'), 
    path('tk/<int:tk_id>', TK_e.as_view(), name='tk_e'), 
    path('tmce/', TMC.as_view(), name='tmc'), 
    path('tmce/<int:tmc_id>', TMC_e.as_view(), name='tmc_e'), 
    path('oper/', OPER.as_view(), name='oper'), 
    # path('company/<slug:company_slug>/', views.company, name='product'),
    # path('company2/<slug:company_slug>/', company2.as_view(), name='company2'),
    path('create-tk/', CreateTK.as_view(), name='create_tk'),
    path('create-tmc/', CreateTMC.as_view(), name='create_tmc'),
    path('create-oper/', CreateOPER.as_view(), name='create_oper'),
    path('create-company/', CreateCompany.as_view(), name='create_company'),
    path('create-user/', CreateUser.as_view(), name='create_user'),
    path('vvid/', vvid.as_view(), name='vvid'),
    path('hello/',views.hello_word_view, name='hyulo'),
    path('', include(router.urls)),

    # path('login/', Login.as_view(), name='login'),
    # path('', include('users.urls',namespace='user')),   
    # path('users/', Users.as_view(), name='users'),
    

]



