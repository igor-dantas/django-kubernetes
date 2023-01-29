from django.db import models
from uuid import uuid4

# criando uma class que será utilizada como modelo pros campos que ficarão disponíveis no banco de dados
class noticias(models.Model):
    # adicionando o campo id que será uma chave primária, hexadecimal e não poderá ser editada
    id_not = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # adicionando o campo titulo do tipo texto, com tamanho máximo de 255 caracteres
    titulo = models.CharField(max_length=255)
    # adicionando o campo conteudo do tipo texto, com tamanho máximo de 255 caracteres
    conteudo = models.CharField(max_length=255)
    # adicionando o campo autor do tipo texto, com tamanho máximo de 255 caracteres
    autor = models.CharField(max_length=255)
    # adicionando campo publicado que será do tipo boolean ou seja true or false
    publicado = models.BooleanField()
    # adicionando o campo de data de criação, que no momento que o registro é criado na api a data é gerada automáticamente
    data_criacao = models.DateTimeField(auto_now_add=True)