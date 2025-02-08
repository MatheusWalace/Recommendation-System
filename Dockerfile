# Usar imagem oficial do Python
FROM python:3.10

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos necessários para dentro do contêiner
COPY requirements.txt .
COPY movies.csv .
COPY movie_recommender.py .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definir comando padrão para rodar o script
CMD ["python", "movie_recommender.py"]
