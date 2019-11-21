import requests
import json

api_token = 'your_api_token'
api_url_base = 'https://my-json-server.typicode.com/ArmandoSA/APITest/db'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():
    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    
    else:
        return None


account_info = get_account_info()

if account_info is not None:
    print(account_info['comments'])
    for a in account_info['comments']:
        print(a['id'])
    print("Here's the information: ")
    for k, v in account_info['profile'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')