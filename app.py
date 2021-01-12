from flask import  Flask
from flask_restful import Api, Resource, reqparse
from requests.exceptions import Timeout
from secrets import token_hex

from objects.camera_requests import  get_camera_image
from objects.image_management import TempImage
import settings

app = Flask(__name__)
api = Api(app)

def api_args():
    """Genera los argumentos necesarios para la API de imagen térmica
    Returns:
        args: args necesarios para peticiones a la API (session, side)
    """
    parser = reqparse.RequestParser()
    parser.add_argument('session', type=str, default=token_hex(8))
    parser.add_argument('side', type=str, choices=('left', 'right', 'center'), default='center')
    return parser.parse_args()

class TIF(Resource):
    """Objeto Resource para API de imagen térmica"""
    def get(self):
        """método GET para el endpoint de la imagen tif
        Returns:
            response: respuesta serializada json
        """
        args = api_args()
        session_name = args['session']
        side = args['side']

        response = {
        'session': session_name,
        'side': side
        }
        try:
            image_path = get_camera_image(session_name, side)
            image = TempImage(image_path)
            response['temperature'] = image.get_center_temperature()
            response['image_url'] = f'http://{settings.HOSTNAME}:{settings.PORT}/static/user_images/{image.save_jpg()}'
            response['error'] = False
            response['status_code'] = 200
        except Exception as e:
            response['error'] = True
            response['status_code'] = 400
            response['reason'] = e.args[0]
        except Timeout as e:
            response['error'] = True
            response['status_code'] = 408
            response['reason'] = e.args[0]
        print(response)
        return response

api.add_resource(TIF, '/image')

if __name__ == '__main__':
    app.run(host=settings.HOSTNAME, port=settings.PORT)