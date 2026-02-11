import requests
import json

API_KEY = 'seam_testf8jm_5Hbb26gfAZXiC5nNETzGzs2P'

accessCodeIdToDelete = input('Please provide Seam access code ID to delete: ')

response = requests.post(
    'https://connect.getseam.com/access_codes/delete',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        },
    json={
        'access_code_id': f'{accessCodeIdToDelete}'
        }
    )

result = response.json()
# accessCode = result['access_code']['code']
# print(f'Access code is: {accessCode}')

print(json.dumps(response.json(), indent=2))