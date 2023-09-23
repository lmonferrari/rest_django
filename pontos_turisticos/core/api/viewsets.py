from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico
from rest_framework.viewsets import ModelViewSet


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # deve retornar um interable (list, queryset, etc)
        return PontoTuristico.objects.filter(aprovado=True)
