from rest_framework.serializers import ModelSerializer

from fabidecor.models import Categoria, Informacoes

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class InformacoesSerializer(ModelSerializer):
    class Meta:
        model = Informacoes
        fields = "__all__"