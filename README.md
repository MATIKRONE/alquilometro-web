# Alquilómetro Web

Un solo servicio de Render sirve la página en `/`, Swagger en `/docs` y
las solicitudes del frontend en `/api/`. `backend/` es una copia del
commit `a9b4c8d` del TP. `web.py` conecta la interfaz a esa aplicación.

## Publicar

1. Subí el contenido de esta carpeta a un repositorio nuevo de GitHub.
   `render.yaml`, `Dockerfile`, `web.py`, `backend/` y `frontend/` deben
   quedar en la raíz. Si usás la interfaz web de GitHub, incluí también
   `.gitignore` y `.dockerignore`.
2. En Render, elegí **+ New → Blueprint** y seleccioná el repositorio nuevo
   y la rama que contiene esos archivos, normalmente `main`.
3. Dejá `render.yaml` como Blueprint Path. Revisá que se cree un único
   servicio Docker llamado `alquilometro-web` con plan Free y desplegalo.
4. Cuando esté Live, abrí su URL pública. Buscá una publicación y abrí su
   ficha. Para probar la API por separado, agregá `/docs` a la misma URL.

Render genera la clave de autenticación. El arranque carga publicaciones
e índices de ejemplo. El plan gratuito usa un disco temporal, así que las
cuentas, publicaciones y contratos de prueba se pueden perder al reiniciar.
