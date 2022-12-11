from django.shortcuts import render, redirect

from django.http import HttpResponse
from rest_framework import  viewsets
from central.models import AlunoTest
from central.serializer import  AlunoSerializer



# Create your views here.
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = AlunoTest.objects.all()
    serializer_class = AlunoSerializer

# pagina incial - rendariing index page
def pageIndex(request):
    return render(request, "index.html")

