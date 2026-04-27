# TeamBoard
## Integrantes:
- Juan Ignacio Piazza
- Ignacio Williams
- Nahuel Fabián Fredes Coronilla
- Avril Lugo Gonzalez
- Alfredo Echeverría

## Instrucciones de uso:

1. Ejecutar el comando `git clone https://github.com/azehor/is-2026-checkpoint-01.git`
2. Acceder al directorio clonado
3. Ejecutar el comando `docker compose up --build -d`
4. Acceder a la direccion `https://localhost:8080` en el navegador

## Servicios:

### 1. Frontend:
El servicio frontend inicia el servidor web `python http.server` para servir la interfaz visual de la aplicación.

### 2. Backend:
El servicio backend inicia un servidor web api usando `Flask` que recibe pedidos de información desde el servicio frontend y consulta a la base de datos para responder dichos pedidos.

### 3. Database:
El servicio database inicia una base de datos `postgres` con los datos iniciales definidos en `database/init.sql` y queda a disposición del servicio backend.

### 4. Portainer:
El servicio portainer habilita una interfaz web para monitorear los servicios docker iniciados sin requerir la terminal o una aplicación estilo Docker Desktop. Una descripción mas detallada y con capturas de pantalla del servicio esta documentada en `portainer/README.md`
