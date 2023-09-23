from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao
from rest_framework.viewsets import ModelViewSet


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
