
from rest_framework.serializers import ModelSerializer

from fabidecor.models import  Informacoes 

class InformacoesSerializer(ModelSerializer):
    class Meta:
        model = Informacoes
        fields = "__all__"
