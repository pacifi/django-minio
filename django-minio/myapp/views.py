from django.shortcuts import render
from rest_framework import serializers, viewsets

from myapp.models import Persona


class PersonaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaModelSerializer
