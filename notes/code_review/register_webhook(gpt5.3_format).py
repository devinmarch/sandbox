import json
import requests


API_KEY = 'cbat_sJ6x5jgymGOnTSybrLbWlp1KUIEMXZhu'
propertyID = '260351'


def postWebhook():
    eventObject = input('Event object: ').strip()
    eventAction = input('Event event: ').strip()
    endpointUrl = input('Enpoint URL: ').strip()

    response = requests.post(
        'https://api.cloudbeds.com/api/v1.3/postWebhook',
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        data={
            'propertyID': f'{propertyID}',
            'object': f'{eventObject}',
            'action': f'{eventAction}',
            'endpointUrl': f'{endpointUrl}',
        },
    )

    if response.status_code == 200:
        result = response.json()
        subscriptionId = result['data']['subscriptionID']
        print(f'Success! Subscription ID is: {subscriptionId}')
        # print(json.dumps(response.json(), indent=2))
    else:
        print(f'Failed: {response.json()}')


def getWebhooks():
    response = requests.get(
        'https://api.cloudbeds.com/api/v1.3/getWebhooks',
        headers={'Authorization': f'Bearer {API_KEY}'},
        data={
            'propertyID': f'{propertyID}',
        },
    )

    if response.status_code == 200:
        result = response.json()

        for webhook in result['data']:
            entity = webhook['event']['entity']
            action = webhook['event']['action']
            url = webhook['subscriptionData']['url']
            webhookId = webhook['id']

            print(f'{entity}/{action} -> {url} (ID: {webhookId})')
        # subscriptionId = result['data']['subscriptionID']
        # print(f'Success! Subscription ID is: {subscriptionId}')
        # print(json.dumps(response.json(), indent=2))
    else:
        print(f'Failed: {response.json()}')


def deleteWebhook():
    webhookId = input('Webhook ID to delete: ').strip()

    response = requests.delete(
        'https://api.cloudbeds.com/api/v1.3/deleteWebhook',
        headers={'Authorization': f'Bearer {API_KEY}'},
        params={
            'propertyIDs': f'{propertyID}',
            'subscriptionID': f'{webhookId}',
        },
    )

    result = response.json()
    if result['success']:
        print('Webhook deleted.')
        # print(json.dumps(response.json(), indent=2))
    else:
        print(f'Failed: {response.json()}')


actionType = input('get, post, or delete webhook:')

if actionType == 'post':
    postWebhook()
elif actionType == 'get':
    getWebhooks()
elif actionType == 'delete':
    deleteWebhook()
else:
    print('Unknown action')
