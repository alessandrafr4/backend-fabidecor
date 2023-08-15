from rest_framework.viewsets import ModelViewSet

from fabidecor.models import Categoria
from fabidecor.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    