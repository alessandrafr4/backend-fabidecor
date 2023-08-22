
from rest_framework.viewsets import ModelViewSet

from fabidecor.models import  Informacoes
from fabidecor.serializers import  InformacoesSerializer

class InformacoesViewSet(ModelViewSet):
    queryset = Informacoes.objects.all()
    serializer_class = InformacoesSerializer 
