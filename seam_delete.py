import requests
import json

API_KEY = 'seam_testf8jm_5Hbb26gfAZXiC5nNETzGzs2P'

response = requests.post(
    'https://connect.getseam.com/access_codes/delete',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        },
    json={
        'access_code_id': 'db708c0c-b1bb-46a0-8eba-a94ab4c367e3'
        }
    )

# result = response.json()
# accessCode = result['access_code']['code']
# print(f'Access code is: {accessCode}')

print(json.dumps(response.json(), indent=2))