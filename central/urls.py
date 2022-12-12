from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.pageIndex, name="home"),
    path('cadastro/', views.pageCadastro, name="cadastro"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)