
from dataclasses import Field
from rest_framework import serializers
from central.models import  JogadorTest

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogadorTest
        fields = ['id', 'name', 'phone', 'code', 'equipa']