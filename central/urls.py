from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.pageIndex, name="home"),
    path('cadastro/', views.pageCadastro, name="cadastro"),
    path('logout/', views.pageLogout, name="logout"),
    path('login/', views.pageLogin, name="login"),
    path('main/', views.pageMain, name="main"),
    #path('cadastroAdd/', views.pageCadastroAdd, name="cadastroAdd"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)