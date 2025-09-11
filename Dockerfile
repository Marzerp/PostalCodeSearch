# Imagen base
FROM python:3.11-slim

# Crear directorio de la app
WORKDIR /app

# Instalar dependencias del sistema (para conectar con MariaDB)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

# Exponer puerto
EXPOSE 5000

# Comando de arranque
CMD ["python", "app.py"]

