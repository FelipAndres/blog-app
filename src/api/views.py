from django.shortcuts import render
from rest_framework import generics
from . serializers import EntradaSerializer
from .models import EntradaModel, ExampleModel


class EntradaView(generics.ListAPIView):
    queryset = EntradaModel.objects.all()
    serializer_class = EntradaSerializer
