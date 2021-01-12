import requests
import shutil
import os
import settings

def get_camera_image(session_name, side):
    """Obtiene y descarga la imagen tif de la api de la cámara
    Args:
        session_name (string): session del usuario dueño de la imagen
    Raises:
        requests.exceptions.Timeout: El servidor no responde dentro del tiempo límite
        Exception: Respuesta vacía del servidor
        Exception: El servidor no respondió correctamente
    Returns:
        string: url de la imagen tif descargada
    """
    fileName = f'{session_name}_{side}.tif'
    save_url = os.path.join(settings.CAMERA_FILES_PATH, fileName)
    try:
        response = requests.get(settings.API_URL, stream=True, timeout=settings.CAMERA_TIMEOUT)
    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout("Camera didn't respond within 20 seconds, try again.")

    if response.status_code == 200:
        response.raw.decode_content = True
        content_length = int(response.raw.getheader('content-length'))
        if not content_length:
            raise Exception('Empty response')
        with open(save_url, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
    else:
        raise Exception(response.reason)
    return save_url


