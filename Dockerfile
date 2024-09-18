# Use a imagem base do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o contêiner
COPY . .

# Exponha a porta na qual o Flask vai rodar
EXPOSE 5000

# Define o comando para iniciar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
