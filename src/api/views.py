# from django.shortcuts import render
# from rest_framework import generics
# from .serializers import EntradaSerializer
# from .models import EntradaModel
# from rest_framework.response import Response

from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializers import *


# class EntradaView(generics.ListAPIView):
#     queryset = EntradaModel.objects.all()
#     serializer_class = EntradaSerializer

#     def post(self, request): 
  
#         serializer = EntradaSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save() 
#             return  Response(serializer.data)
class ReactView(APIView): 
    
    serializer_class = EntradaSerializer 
  
    def get(self, request): 
        entrada = [ {"autor": entrada.autor,"titulo": entrada.titulo, "cuerpo": entrada.cuerpo}  
        for entrada in EntradaModel.objects.all()] 
        return Response(entrada) 
  
    def post(self, request): 
  
        serializer = EntradaSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 