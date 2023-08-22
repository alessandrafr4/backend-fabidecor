
from rest_framework.viewsets import ModelViewSet

from fabidecor.models import Temas
from fabidecor.serializers import TemasListSerializer, TemasSerializer, TemasDetailSerializer

class TemasViewSet(ModelViewSet):
    queryset = Temas.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TemasListSerializer
        elif self.action == "retrieve":
            return TemasDetailSerializer
        return TemasSerializer
    
