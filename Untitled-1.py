import request
import json

api_token = 'your_api_token'
api_url_base = 'https://my-json-server.typicode.com/ArmandoSA/APITest/db
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None