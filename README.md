# CHALLENGE BACKEND DEVELOPER

## PROYECTO A REALIZAR

El objetivo del proyecto es crear una API que permita realizar un CRUD de usuarios. Los usuarios se almacenan en un archivo JSON que hace las veces de base de datos. Cada usuario tiene un id, un username, un mail y una contraseña, que deben ser únicos. Además, la API permite al usuario loguearse con su username y contraseña y obtener un token, y consultar si su token es válido mediante un endpoint específico. También se implementa una funcionalidad optativa que se describe más adelante.

## TECNOLOGÍAS UTILIZADAS

- Python
- Flask
- JWT
- Werkzeug (para hashear las contraseñas)

## INSTALACIÓN DE DEPENDENCIAS

Para instalar las dependencias del proyecto, se recomienda crear un entorno virtual con `virtualenv` y luego ejecutar el siguiente comando:

`pip install -r requirements.txt`


## EJECUCIÓN DEL PROYECTO

Para ejecutar el proyecto, se debe ejecutar el siguiente comando desde la carpeta raíz:

`python app.py`


Esto iniciará el servidor Flask en el puerto 5000. Se puede acceder a la API mediante las siguientes rutas:

- `/login` (POST): Permite al usuario loguearse con su username y contraseña y obtener un token si son válidos.
- `/puedopasar/<username>` (GET): Verifica si el token enviado en el encabezado Authorization es válido para el usuario indicado por el parámetro `<username>`. Devuelve true si es válido, false si no lo es o ha expirado, o un mensaje de error si faltan datos.
- `/user` (POST): Crea un nuevo usuario con los datos enviados en el cuerpo de la petición. Los datos deben incluir username, mail, password y admin (este último indica si el usuario es administrador o no, por defecto es false).
- `/user/<user_id>` (GET): Obtiene los datos de un usuario por su id.
- `/users` (GET): Obtiene la lista de todos los usuarios registrados.
- `/user/<user_id>` (PUT): Actualiza los datos de un usuario por su id con los datos enviados en el cuerpo de la petición. Los datos pueden incluir username, mail, password o admin.
- `/user/<user_id>` (PATCH): Elimina lógicamente un usuario por su id, cambiando su atributo active a false.
- `/user/<user_id>` (DELETE): Elimina permanentemente un usuario por su id.
- `/user/solicitarPermisos/<user_id>` (POST): Solicita permisos de administrador para el usuario indicado por el parámetro `<user_id>`. El usuario debe tener un token válido y no ser administrador previamente.
- `/admin/obtenerPermisos` (GET): Obtiene la lista de los usuarios que han solicitado permisos de administrador. El usuario debe tener un token válido y ser administrador.
- `/admin/darPermisos/<user_id>` (POST): Otorga permisos de administrador al usuario indicado por el parámetro `<user_id>`. El usuario debe tener un token válido, ser administrador y haber solicitado previamente los permisos.

## DOCUMENTACIÓN DE LAS REQUESTS

Para ver ejemplos de las requests y sus respuestas, se puede consultar el archivo `documentacion.pdf` que se encuentra en la carpeta raíz del proyecto.
