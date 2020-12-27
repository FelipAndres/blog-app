from django.shortcuts import render
from rest_framework import generics
from .serializers import EntradaSerializer
from .models import EntradaModel
from rest_framework.response import Response


class EntradaView(generics.ListAPIView):
    queryset = EntradaModel.objects.all()
    serializer_class = EntradaSerializer

    def post(self, request): 
  
        serializer = EntradaSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 