import requests

response = requests.get('http://127.0.0.1:5000/image/asd-fgh-jkl/left')
print(response.json())
