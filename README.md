
# Proyecto FastAPI con Docker y PostgreSQL

Este proyecto es una API basada en FastAPI, que utiliza una base de datos PostgreSQL. El sistema permite la creación, actualización y gestión de tareas de usuarios. La API también integra la obtención de información del clima mediante la API de OpenWeather.

## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postman](https://www.postman.com/) (Opcional, para pruebas de la API)

## Configuración

### Variables de Entorno

El proyecto utiliza variables de entorno para configuraciones sensibles como claves secretas y APIs. Asegúrate de incluir lo siguiente en tu archivo `docker-compose.yml` o en tu entorno:

- `SECRET_KEY`: Clave secreta para la autenticación.
- `OPENWEATHER_API_KEY`: Clave de la API de OpenWeather para obtener información meteorológica.


## Ejecución del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto
```

### 2. Configurar las variables de entorno

Modifica el archivo `docker-compose.yml` con tus propias credenciales de base de datos y claves:

```yaml
services:
  web:
    environment:
      - DATABASE_URL=postgresql://usuario:contraseña@db:5432/nombre_base_de_datos
      - SECRET_KEY=tu_clave_secreta
      - OPENWEATHER_API_KEY=tu_clave_openweather
```

### 3. Construir y levantar los servicios con Docker

```bash
docker-compose up --build
```

Esto levantará la aplicación FastAPI en el puerto `8000` y PostgreSQL en el puerto `5432`.

### 4. Aplicar migraciones con Alembic

Después de que el contenedor esté en funcionamiento, aplica las migraciones a la base de datos:

```bash
docker-compose exec web alembic upgrade head
```

## Documentación de la API

### Endpoints Disponibles

1. **Autenticación**

   - **POST** `/token`: Autenticación del usuario mediante nombre de usuario y contraseña.
     - Cuerpo de la solicitud (JSON):
       ```json
       {
         "username": "string",
         "password": "string"
       }
       ```
     - Respuesta (JSON):
       ```json
       {
         "access_token": "string",
         "token_type": "bearer"
       }
       ```

2. **Tareas**

   - **POST** `/tasks`: Crear una nueva tarea para el usuario autenticado.
     - Cuerpo de la solicitud (JSON):
       ```json
       {
         "task_name": "Comprar alimentos",
         "description": "Comprar frutas y vegetales en el supermercado"
       }
       ```
     - Respuesta (JSON):
       ```json
       {
         "id": "UUID",
         "task_name": "Comprar alimentos",
         "status": "pending",
         "ip_address": "xxx.xxx.xxx.xxx",
         "country": "CU",
         "weather": "few clouds, 24.4°C",
         "user_id": "UUID"
       }
       ```

   - **GET** `/tasks`: Obtener todas las tareas del usuario autenticado.

   - **PUT** `/tasks/{task_id}`: Actualizar una tarea existente.

   - **DELETE** `/tasks/{task_id}`: Eliminar una tarea.

### Archivos JSON de Ejemplo

- Solicitud de creación de tarea:
  ```json
  {
    "task_name": "Comprar alimentos",
    "description": "Comprar frutas y vegetales en el supermercado"
  }
  ```

- Respuesta de creación de tarea:
  ```json
  {
    "id": "26c94a30-233f-4c3c-b577-13f42bbc15ad",
    "task_name": "Comprar alimentos",
    "status": "pending",
    "ip_address": "152.207.246.33",
    "country": "CU",
    "weather": "few clouds, 24.4°C",
    "user_id": "e891e9db-7645-4907-afcc-b6faa7703371"
  }
  ```

## Archivos Postman

Puedes importar los archivos de colección de Postman para probar la API con las siguientes solicitudes predefinidas.

1. Descarga los archivos JSON de colección:
   - [Colección de Postman de la API](./postman_collection.json)

2. Importa la colección a Postman:
   - Abre Postman y selecciona **Importar**.
   - Carga el archivo `postman_collection.json`.

## Testing

Para ejecutar pruebas locales, puedes utilizar `pytest`. Asegúrate de que los servicios de Docker estén en funcionamiento:

```bash
docker-compose exec web pytest
```

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama para tu característica o corrección de error: `git checkout -b mi-nueva-rama`.
3. Realiza tus cambios y haz commit: `git commit -m "Añadí una nueva característica"`.
4. Sube tu rama: `git push origin mi-nueva-rama`.
5. Abre un pull request.


