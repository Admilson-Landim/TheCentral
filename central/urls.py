from django.contrib import admin
from django.urls import path, include
from central.views import AlunoViewSet
from rest_framework import routers

from config import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)


urlpatterns = [
    path('', views.pageIndex, name="home"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)