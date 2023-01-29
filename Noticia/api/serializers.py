from rest_framework import serializers
from Noticia import models

# construindo uma class serializer que tem como intuito converter uma estrutura de dados ou um objeto em um formato que possa ser armazenado ou transferido
class noticiasSerializer(serializers.ModelSerializer):
    class Meta:
        # estou indicando o models noticias que eu criei 
        model = models.noticias
        # estou indicando que quero que todos os campos sejam traduzidos
        fields = '__all__'