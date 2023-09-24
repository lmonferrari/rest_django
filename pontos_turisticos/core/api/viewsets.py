from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # deve retornar um interable (list, queryset, etc)

        queryset = PontoTuristico.objects.all()

        filter_params = ["id", "nome", "descricao"]
        for param in filter_params:
            if self.request.query_params.get(param, None):
                queryset = queryset.filter(
                    **{
                        param: self.request.query_params[param],
                    }
                )

        return queryset

    # #sobrescrevendo o metodo list
    # def list(self, request, *args, **kwargs):
    #     return Response({"teste": 123})

    # # sobrescrevendo o metodo create
    # def create(self, request, *args, **kwargs):
    #     return Response({"Hello": request.data["nome"]})

    # # sobrescrevendo o metodo destroy
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # # sobrescrevendo o metodo update
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # # sobrescrevendo o metodo update
    # def update(self, request, *args, **kwargs):
    #     pass

    # # sobrescrevendo o metodo partial_update
    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # função customizada para denunciar um ponto turistico
    # detail = True para que o endpoint seja
    # acessivel apenas para um ponto turistico
    # detail = False para que o endpoint seja
    # acessivel para todos os pontos turisticos
    # uri: http://localhost:8000/pontoturistico/1/denunciar/
    @action(methods=["get"], detail=True)
    def denunciar(self, request, pk=None):
        return Response({"Denunciar": pk})
