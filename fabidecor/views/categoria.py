from rest_framework.viewsets import ModelViewSet

from fabidecor.models import Categoria,Categoria
from fabidecor.serializers import  CategoriaSerializer, CategoriaSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer 

# class CategoriaViewSet(ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer 
#     permission_classes = [IsAuthenticated]
 