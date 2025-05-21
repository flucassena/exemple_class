# Dockerfile para projeto Django

# Imagem base com Python
FROM python:3.10-slim

# Variáveis de ambiente para otimização
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o requirements e instala pacotes Python
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia todo o código do projeto para dentro do container
COPY . /app/

# Expondo a porta padrão do Django
EXPOSE 8000

# Comando padrão: aplica migrations e inicia o servidor de desenvolvimento
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
