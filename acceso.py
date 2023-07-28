import requests
import base64

client_id = '50b1f20182a948419c66e209362c7671'
client_secret = 'a32952f1e8e54510a28c7bcc960604ac'

# Codificamos en base64 nuestras credenciales
credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

if response.status_code != 200:
    print(f'Error en la solicitud: {response.status_code}')
else:
    token_data = response.json()
    access_token = token_data['access_token']
    print(f'Token de acceso: {access_token}')


#BQAF4wW0ytywb2FvIqQ1A21D-PKGWSiYen2hk-DBFSJwSKz7DwX0knNeLSr4KJiV7_GAOr95znSszF5iwb1WIe6l9ypJY4Lp7t6InyDpvksK-TUn3cs