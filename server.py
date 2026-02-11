from flask import Flask, request
import json
import requests
from database import RoomBlockCode

SEAM_API_KEY = 'seam_testf8jm_5Hbb26gfAZXiC5nNETzGzs2P'

SEAM_DEVICE_ID = {
    '537928-1': '64c74161-80e9-4877-83fc-7b38b7e4cdce',
    '537928-2': '4dc2c282-85ce-459d-8b89-e8ac254d5a4a',
    '537928-3': 'b2c8ebef-d4b1-4077-ac30-c588daa715eb'
}

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.get_json()

    reason = data['roomBlockReason'].strip().lower()
    blockId = data['roomBlockID']
    blockType = data['roomBlockType']
    eventType = data['event']
    room = data['rooms'][0]['roomID']

    if blockType == 'out_of_service' and reason == 'guinness' and eventType == 'roomblock/created':

        response = requests.post(
            'https://connect.getseam.com/access_codes/create',
            headers={
                'Authorization': f'Bearer {SEAM_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'device_id': SEAM_DEVICE_ID[room]
            }
        )

        result = response.json()
        accessCode = result['access_code']['code']
        accessCodeId = result['access_code']['access_code_id']

        RoomBlockCode.create(block_id=blockId, access_code_id=accessCodeId, access_code=accessCode, room_id=room)
            
        print(f"Access code: {accessCode} was installed and stored for {room}")

    elif blockType == 'out_of_service' and eventType == 'roomblock/removed':
        
        record = RoomBlockCode.get_or_none(RoomBlockCode.block_id == blockId)

        if record:

            response =  requests.post(
                'https://connect.getseam.com/access_codes/delete',
                headers={
                'Authorization': f'Bearer {SEAM_API_KEY}',
                'Content-Type': 'application/json'
                }, 
                json={
                    'access_code_id': record.access_code_id
                }
            )

            # result = response.json()
            if response.status_code == 200:
                 record.delete_instance()
                 print(f'Code deleted for Room ID: {room}')
            

        else:
             print('No access code ID found in storage.')

    else:
        print(f"Room blocked skipped.")
    return '', 200




if __name__ == '__main__':
    app.run(debug=True, port=5002)