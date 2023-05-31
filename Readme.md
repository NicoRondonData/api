# Eejcutar le proyecto
Para correr el proyecto es necesario tener docker instalado

```bash
docker-compose up -d
```

Pare ejecutar la suite de pruebas levanta el proyecto con el comando anterior y ejecuta lo siguiente
```bash
docker exec -it djangoapi-django-1 pytest -s -v
```

Luego de ejecutar el proyecto puedes encontar su documentacion en
http://127.0.0.1:8000/api/schema/docs/

Etoken debe iniciar con Bearer y enviarse en el header de autenticacion

Bearer {Token}
# Objetivo:

Desarrollar una API RESTful para una plataforma de blog con funcionalidades
avanzadas utilizando Django REST Framework y Python como lenguaje de
programación principal.

## Descripción del Proyecto:

La plataforma de blog consta de varias entidades: Usuarios, Perﬁles, Entradas (Posts),
Comentarios y Likes. Los Usuarios pueden tener roles de administrador, editor o
blogger. Los Usuarios tienen un Perﬁl asociado con información adicional como la
biografía y la imagen de perﬁl. Las Entradas están asociadas a un Usuario (el autor) e
incluyen un título, contenido, fecha de publicación, categoría y una lista de etiquetas
(tags). Los Comentarios están vinculados a un Usuario (la persona que comenta) y a
una Entrada, e incluyen el texto del comentario. Los Usuarios pueden dar Like tanto a
Entradas como a Comentarios.

## Requisitos del proyecto:

1. **Modelado de Datos**: Diseña e implementa modelos de datos para Usuario, Perﬁl, Entrada, Comentario y Like.

2. **Autenticación y Autorización**: Implementa un sistema de autenticación y
 autorización que permita a los administradores gestionar todos los recursos, a
 los editores gestionar Entradas, Comentarios y Likes, y a los bloggers crear y
 gestionar sus propias Entradas, Comentarios y Likes.

3. **API Endpoints**: Implementa los siguientes endpoints:

 - CRUD de Usuarios y Perﬁles
 - CRUD de Entradas
 - CRUD de Comentarios
 - CRUD de Likes

4. **Serialización**: Emplea los serializadores de Django REST para manejar la conversión entre modelos y JSON.

5. **Filtros y Paginación**: Implementa ﬁltros que permitan buscar entradas por título,
 autor, categoría y etiquetas. Además, implementa la paginación en los endpoints
 que devuelven múltiples recursos.

6. **Pruebas**: Desarrolla pruebas unitarias y de integración para los modelos, la autenticación, la autorización y los endpoints de la API. Asegúrate de cubrir tanto
los casos de éxito como los de error.




7. **Documentación**: Documenta todos los endpoints de la API utilizando Django REST Swagger o similar.

### Instrucciones de entrega:

Por favor, sube tu solución a un repositorio de GitHub y comparte el enlace con
nosotros. Asegúrate de incluir un archivo README con instrucciones detalladas sobre
cómo instalar y ejecutar el proyecto, cómo ejecutar las pruebas, y cualquier información
relevante.
