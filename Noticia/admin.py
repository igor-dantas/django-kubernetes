from django.contrib import admin
from Noticia.models import noticias

class Noticia(admin.ModelAdmin):
    # configurando campos que estarão visíveis no admin do django
    list_display = ('id_not', 'titulo', 'conteudo', 'autor', 'publicado', 'data_criacao')
    # adicionando campos que funcionaram como uma espécie de link, que ao serem clicados poderão ser editados os dados, ou até mesmo apagados
    list_display_links = ('id_not',)
    # adicionando campos de pesquisa
    search_fields = ('id_not', 'titulo',)
# registrando minha api de Noticia com o models noticias no admin do django
admin.site.register(noticias, Noticia)