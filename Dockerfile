# Usamos una imagen oficial de Python como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos requeridos para la aplicación
COPY requirements.txt .

# Instalamos las dependencias, incluyendo Alembic
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . .

# Exponemos el puerto en el que correrá la app
EXPOSE 8000

# Comando para aplicar migraciones con Alembic y ejecutar la aplicación
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
