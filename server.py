from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    reason = data['roomBlockReason']
    if data['roomBlockType'] == 'out_of_service':
        print(f"An OUT OF SERVICE block with reason: {reason}")
    else:
        print(f"A ROOM BLOCK with reason: {reason}")
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, port=5002)