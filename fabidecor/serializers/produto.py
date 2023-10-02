from rest_framework.serializers import ModelSerializer

from fabidecor.models import Produto
from uploader.models import Image

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto 
        fields = "__all__"
  
