from django.shortcuts import render, redirect

from django.http import HttpResponse
from rest_framework import  viewsets
from central.models import JogadorTest
from central.serializer import  JogadorSerializer



# Create your views here.
class JogadorViewSet(viewsets.ModelViewSet):
    queryset = JogadorTest.objects.all()
    serializer_class = JogadorSerializer

# pagina incial - rendariing index page
def pageIndex(request):
    return render(request, "index.html")

