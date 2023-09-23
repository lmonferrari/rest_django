from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from rest_framework.viewsets import ModelViewSet


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
