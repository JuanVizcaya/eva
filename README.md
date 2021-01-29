# Imagen térmica
Es una app "Flask/flask_restful", donde su principal función es hacer peticiones al servidor de una cámara termográfica para procesar y almacenar una imagen .tif y convertirla a jpg.
La API responde con un "json" que contiene los atributos de la petición y de la imagen.

## Requisitos
#### Se requiere la versión correcta de Python.
- Python 3.7.9
##### Creación de un entorno virtual con Anaconda:
`conda create -n eva python=3.7.9`

`conda activate eva`
##### Creación de un entorno virtual con virtualenv:
`virtualenv eva --python=python3.7.9`

`source eva/bin/activate`

## Instalación
1. Clonar proyecto: 
`git clone https://github.com/JuanVizcaya/eva.git`

2. Entrar a la carpeta "eva": 
`cd eva`

3. Instalar librerías de python: 
`pip install -r requirements.txt`

## Ejecución
- Ejecutar dentro de la carpeta "eva": `python app.py`
```
* Serving Flask app "app" (lazy loading)
* Environment: production
 WARNING: This is a development server. Do not use it in a production deployment.
 Use a production WSGI server instead.
* Debug mode: off
* Running on http://localhost:4700/ (Press CTRL+C to quit)
```
## Utilización
Cuando el servidor virtual se encuentra corriendo de manera correcta, se puede enviar una petición a la API de imagen térmica.

#### Endpoint:
`GET: http://localhost:4700/image`

#### Parámetros:
| Nombre | Tipo | Requerido | Default | Descripción
| ----------- | ----------- | ----------- | ----------- | ------------------- |
| **session** | Text | Opcional | Token único hexadecimal | ID de sesión relacionada con el usuario. |
| **side** | Text |  Opcional  | center | Lado en el que se tomó la imagen, opciones: left, right, center. |

**Nota:** Dichos parámetros son opcionales, sin embargo, es preferible enviarlos para que la imagen se guarde con sus atributos correctos.

#### Ejemplo:
`http://localhost:4700/image?session=jgstbh-4jfk-lkfds&side=left`

*Respuesta:*
```
{
  "session": "jgstbh-4jfk-lkfds",
  "side": "left",
  "temperature": 34.69,
  "image_url": "http://localhost:4700/static/user_images/jgstbh-4jfk-lkfds_left.jpg",
  "error": false,
  "status_code": 200
}
```

**Nota:** La url de la imagen ("image_url") queda disponible para su descarga y/o posible visualización, en una pestaña del navegador.
