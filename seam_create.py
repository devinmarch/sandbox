import requests
import json

API_KEY = 'seam_testf8jm_5Hbb26gfAZXiC5nNETzGzs2P'

response = requests.post(
    'https://connect.getseam.com/access_codes/create',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        },
    json={
        'device_id': '64c74161-80e9-4877-83fc-7b38b7e4cdce'
        }
    )

result = response.json()
accessCode = result['access_code']['code']
print(f'Access code is: {accessCode}')

## print(json.dumps(response.json(), indent=2))