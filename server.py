from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"A roomblock was created with the following reason: {data['roomBlockReason']}")

if __name__ == '__main__':
    app.run(debug=True, port=5002)