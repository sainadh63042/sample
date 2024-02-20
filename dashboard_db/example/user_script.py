import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def send_message(source, message):
    url = 'http://192.168.1.100:5000/send_message'
    data = {'source': source, 'message': message}
    response = requests.post(url, json=data)
    print(response.json())


def get_user_messages():
    url = 'http://192.168.1.100:5000/get_user_messages'
    response = requests.post(url, json={'source': 'example'})  # Provide a default source for the example
    user_messages = response.json().get('user_messages', [])
    return user_messages


@app.route('/')
def index():
    return render_template('user_input.html')


@app.route('/send_message', methods=['POST'])
def send_message_route():
    source = request.form['source']
    message = request.form['message']

    send_message(source, message)

    return render_template('user_input.html')


@app.route('/user_messages')
def user_messages():
    user_messages = get_user_messages()
    return render_template('user_messages.html', user_messages=user_messages)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
