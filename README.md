# 🎬 Sistema de Recomendação de Filmes

Este projeto implementa um sistema de recomendação de filmes utilizando **Python**, **Pandas**, **Scikit-Learn** e **Docker**.

## 🚀 Tecnologias Utilizadas
- Python 3.10
- Pandas
- NumPy
- Scikit-Learn
- Docker

## 📂 Estrutura do Projeto
```
📂 movie-recommender
│-- 📄 Dockerfile
│-- 📄 requirements.txt
│-- 📄 movies.csv
│-- 📄 movie_recommender.py
```

## 📥 Instalação e Execução
### 1️⃣ Clonar o repositório
```sh
git clone https://github.com/seu-usuario/movie-recommender.git
cd movie-recommender
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Executar o sistema de recomendação
```sh
python movie_recommender.py
```

## 🐳 Executando com Docker
### 1️⃣ Construir a imagem
```sh
docker build -t movie-recommender .
```

### 2️⃣ Rodar o contêiner
```sh
docker run --rm movie-recommender
```

## 📊 Como Funciona?
1. O script lê o arquivo `movies.csv` com uma lista de filmes, gêneros e avaliações.
2. Ele processa os gêneros usando **TF-IDF** e calcula similaridades entre filmes.
3. O usuário pode inserir um título de filme e receber recomendações baseadas em similaridade.

## 🎯 Exemplo de Uso
```sh
Filmes recomendados para 'The Matrix':
- Inception
- Interstellar
- Avatar
```

## 📜 Licença
Este projeto é open-source e está sob a licença MIT. Sinta-se livre para contribuir! 🚀
