from rest_framework.serializers import ModelSerializer

from fabidecor.models import  Catalago 

class CatalagoSerializer(ModelSerializer):
    class Meta:
        model = Catalago 
        fields = "__all__"
