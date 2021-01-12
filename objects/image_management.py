from PIL import Image
from os.path import join, basename
import numpy as np
import settings

class TempImage:
    """Objeto para manipulación de imagen tif"""
    def __init__(self, image_path):
        """Inicializa objeto para manipulación de imagen tif
        Args:
            image_path (string): ubicación de la imagen a manipular
        """
        self.image = Image.open(image_path)
        self.image_array = np.array(self.image)

    def save_jpg(self):
        """Exporta la imagen tif en formato JPEG para ser visualizada online
        Returns:
            string: nombre de la imagen exportada en JPEG
        """
        outImage = self.image
        jpgName = f'{basename(outImage.filename).split(".")[0]}.jpg'
        outFile = join(settings.USER_IMAGES_PATH, jpgName)
        outImage.mode = 'I'
        out = outImage.point(lambda i:i*(1./256)).convert('L')
        out.save(outFile, "JPEG", quality=100)
        return jpgName

    def get_center_temperature(self):
        """Obtiene la temperatura en el centro de la imagen tif
        Returns:
            float: temperatura del centro de la imagen en grados celsius con 2 decimales
        """
        x,y = self.image_array.shape
        center_value = self.image_array[int(x/2)][int(y/2)]
        center_value_shifted = center_value >> 2
        center_temperature = round((center_value_shifted * 0.04) - 273.15, 2)
        return center_temperature