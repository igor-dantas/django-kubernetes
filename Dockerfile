# imagem base que será utilizada
FROM python:3.10.0

# criando um diretório
RUN mkdir /API-Django-Rest
# definindo váriaveis de ambiente
# python não gera arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# as mensagens de log não ficaram armazenadas em buffers
ENV PYTHONUNBUFFERED 1

# definindo o diretório
WORKDIR /API-Django-Rest

# copia o requirements para o diretório /API-Django-Rest
COPY requirements.txt .
# intalar as dependencias do projeto
RUN pip install -r requirements.txt

# copia tudo que está na pasta local e envia para o diretório /API-Django-Rest
COPY . .

# Expondo porta do django
EXPOSE 8000