from pathlib import Path
import os

"""Archivo con configuraciones generales necesarias para la ejecución del aplicativo"""

# Directorio base de la app
BASE_DIR = Path(__file__).resolve().parent

# Nombre del servidor
HOSTNAME = 'localhost'
PORT = 4700

# Ubicación de imagenes
CAMERA_FILES_PATH = os.path.join(BASE_DIR, 'source_images')
USER_IMAGES_PATH = os.path.join(BASE_DIR, 'static', 'user_images')
CAMERA_TIMEOUT = 20

# Endpoint de la cámara
API_URL = 'https://fake-img-endpoint.vercel.app/api/image'