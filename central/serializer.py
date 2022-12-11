
from dataclasses import Field
from rest_framework import serializers
from central.models import  AlunoTest

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoTest
        fields = ['id', 'name', 'phone', 'code']