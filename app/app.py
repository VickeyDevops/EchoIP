from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_public_ip():
    ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
    return f"Public IP: {ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
