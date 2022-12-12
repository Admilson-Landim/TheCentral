from django.shortcuts import render, redirect

from django.http import HttpResponse
from rest_framework import  viewsets
from central.models import JogadorTest, Utilizador
from central.serializer import  JogadorSerializer, UtilizadorSerializer
from django.contrib.auth.models import User
from django.contrib import messages



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
def pageCadastroAdd(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        #csenha = request.POST.get('csenha')

        #try com model User.... 29:50
        novoUser = Utilizador.objects.create(name, phone, email, senha)
        novoUser.save()

        messages.success(request, " Conta criado com sucesso !!!")
        #return redirect('home')
    

    #fields = ['id', 'name', 'phone', 'email', 'senha']
    #return render(request, "cadastro.html")


# pagina incial - rendariing index page
def pageCadastro(request):
    return render(request, "cadastro.html")

# pagina incial - rendariing index page
def pageLogout(request):
    return render(request, "index.html")
