from django.shortcuts import render, redirect

from django.http import HttpResponse
from rest_framework import  viewsets
from central.models import JogadorTest, Utilizador
from central.serializer import  JogadorSerializer, UtilizadorSerializer



# Create your views here.
class UtilizadorViewSet(viewsets.ModelViewSet):
    queryset = Utilizador.objects.all()
    serializer_class = UtilizadorSerializer

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = JogadorTest.objects.all()
    serializer_class = JogadorSerializer


# pagina incial - rendariing index page
def pageIndex(request):
    return render(request, "index.html")

# pagina incial - rendariing index page
def pageCadastro(request):
    return render(request, "cadastro.html")

