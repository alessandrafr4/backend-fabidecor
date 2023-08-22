from rest_framework.serializers import ModelSerializer

from fabidecor.models import Temas

class TemasSerializer(ModelSerializer):
    class Meta:
        model = Temas
        fields = "__all__"

class TemasDetailSerializer(ModelSerializer):
    class Meta:
        model = Temas
        fields = "__all__"
        depth= 1

class TemasListSerializer(ModelSerializer):
    class Meta:
        model = Temas
        fields = ["id","modelo"]