
import mysql.connector
from django.shortcuts import render, redirect

from django.http import HttpResponse
from rest_framework import  viewsets
from central.models import JogadorTest, Utilizador
from central.serializer import  JogadorSerializer, UtilizadorSerializer
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login



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
        names = request.POST.get('name')
        phones = request.POST.get('phone')
        emails = request.POST.get('email')
        senha = request.POST.get('senha')
        #csenha = request.POST.get('csenha')

        #try com model User.... 29:50
        novoUser = Utilizador.objects.create(name=names, phone=phones, email=emails, senha=senha)
        novoUser.save()

        messages.success(request, "Conta criado com sucesso !!!")
        return redirect('home')
    # End pageCadastroAdd


# pagina incial - rendariing index page
def pageCadastro(request):

    if request.method == "POST":
        names = request.POST.get('name')
        phones = request.POST.get('phone')
        emails = request.POST.get('email')
        senha = request.POST.get('senha')
        #csenha = request.POST.get('csenha')

        #try com model User.... 29:50
        novoUser = Utilizador.objects.create(name=names, phone=phones, email=emails, senha=senha)
        novoUser.save()

        messages.success(request, "Conta criado com sucesso !!!")
        return redirect('home')

    return render(request, "cadastro.html")

# pagina incial - rendariing index page
def pageLogout(request):
    return render(request, "index.html")

# pagina login - rendariing index page
def pageLogin(request):

    if request.method == "POST":
        emails = request.POST.get('')
        senhas = request.POST.get('')

        user = authenticate(request, email=emails, senha=senhas)
        #user01 = login(request, user)

        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» email00: ", emails)
        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» senha00: ", senhas)
        #print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» Utilizador00: ", Utilizador)
        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» User00: ", user)
        #print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» User01: ", user01)

        if user is not None:
            print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» senha: ", senhas)
            login(request, user)
            name = user.name
            print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» name: ", name)
            return render(request, "main.html", {'email': emails, 'name': name})

        else:
            print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» Not !!! Login Failed")
            messages.error(request, "Credencial errado !!!")
            return redirect('home')

    return render(request, "index.html")



# pagina incial - rendariing index page
def pageMain(request):
    return render(request, "main.html")
