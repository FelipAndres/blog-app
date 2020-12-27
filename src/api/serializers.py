from rest_framework import serializers
from .models import EntradaModel


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaModel
        fields = ('autor', 'titulo',
                  'cuerpo')