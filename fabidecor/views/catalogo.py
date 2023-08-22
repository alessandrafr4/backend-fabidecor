from rest_framework.viewsets import ModelViewSet

from fabidecor.models import  Catalago
from fabidecor.serializers import  CatalagoSerializer

class CatalagoViewSet(ModelViewSet):
    queryset = Catalago.objects.all()
    serializer_class = CatalagoSerializer 