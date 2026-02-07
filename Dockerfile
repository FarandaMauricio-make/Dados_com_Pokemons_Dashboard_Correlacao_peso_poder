# Usar imagem oficial do Python (leve e atualizada)
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos necessários para dentro do container
COPY requirements.txt .
COPY Pokemon_peso_poder.py .
COPY pokemon_dw.db .

# Instalar dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar o app Streamlit
CMD ["streamlit", "run", "Pokemon_peso_poder.py", "--server.port=8501", "--server.address=0.0.0.0"]
