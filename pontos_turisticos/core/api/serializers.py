from core.models import PontoTuristico
from rest_framework.serializers import ModelSerializer


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = "__all__"
