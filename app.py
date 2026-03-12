from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>AI Agent Deployed This Website!</h1><p>Status: Online</p>"

@app.route('/health')
def health():
    return jsonify(status="UP", version="1.0.0")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
