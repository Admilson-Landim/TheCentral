
from dataclasses import Field
from rest_framework import serializers
from central.models import  JogadorTest, Utilizador

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogadorTest
        fields = ['id', 'name', 'phone', 'code', 'equipa']


class UtilizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizador
        fields = ['id', 'name', 'phone', 'email', 'senha']