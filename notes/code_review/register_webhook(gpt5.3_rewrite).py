import json

import requests


API_KEY = 'cbat_sJ6x5jgymGOnTSybrLbWlp1KUIEMXZhu'
PROPERTY_ID = '260351'
BASE_URL = 'https://api.cloudbeds.com/api/v1.3'


def _auth_headers(content_type=None):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    if content_type:
        headers['Content-Type'] = content_type
    return headers


def _json_or_text(response):
    try:
        return response.json()
    except ValueError:
        return response.text


def post_webhook():
    event_object = input('Event object: ').strip()
    event_action = input('Event event: ').strip()
    endpoint_url = input('Enpoint URL: ').strip()

    response = requests.post(
        f'{BASE_URL}/postWebhook',
        headers=_auth_headers('application/x-www-form-urlencoded'),
        data={
            'propertyID': PROPERTY_ID,
            'object': event_object,
            'action': event_action,
            'endpointUrl': endpoint_url,
        },
    )

    if response.status_code == 200:
        result = response.json()
        subscription_id = result['data']['subscriptionID']
        print(f'Success! Subscription ID is: {subscription_id}')
    else:
        print(f'Failed: {_json_or_text(response)}')


def get_webhooks():
    response = requests.get(
        f'{BASE_URL}/getWebhooks',
        headers=_auth_headers(),
        data={'propertyID': PROPERTY_ID},
    )

    if response.status_code == 200:
        result = response.json()
        for webhook in result['data']:
            entity = webhook['event']['entity']
            action = webhook['event']['action']
            url = webhook['subscriptionData']['url']
            webhook_id = webhook['id']
            print(f'{entity}/{action} -> {url} (ID: {webhook_id})')
    else:
        print(f'Failed: {_json_or_text(response)}')


def delete_webhook():
    webhook_id = input('Webhook ID to delete: ').strip()

    response = requests.delete(
        f'{BASE_URL}/deleteWebhook',
        headers=_auth_headers(),
        params={
            'propertyIDs': PROPERTY_ID,
            'subscriptionID': webhook_id,
        },
    )

    result = _json_or_text(response)
    if isinstance(result, dict) and result.get('success'):
        print('Webhook deleted.')
    else:
        print(f'Failed: {result}')


def main():
    actions = {
        'post': post_webhook,
        'get': get_webhooks,
        'delete': delete_webhook,
    }

    action_type = input('get, post, or delete webhook:').strip().lower()
    action = actions.get(action_type)

    if action:
        action()
    else:
        print('Unknown action')


if __name__ == '__main__':
    main()
