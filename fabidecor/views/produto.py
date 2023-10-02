from rest_framework.viewsets import ModelViewSet

from fabidecor.models import Produto
from fabidecor.serializers import  ProdutoSerializer
from rest_framework.permissions import IsAuthenticated

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer 
