from rest_framework import viewsets
from Noticia.api import serializers
from Noticia import models
# criando uma classe view sets que irá definir quais operações estarão disponíveis
class noticiasViewSet(viewsets.ModelViewSet):
    # importando minha classe serializer para uso do formato json
    serializer_class = serializers.noticiasSerializer
    # solicitando todos os meus objetos criados no models
    queryset = models.noticias.objects.all()