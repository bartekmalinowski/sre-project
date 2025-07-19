from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to the SRE Project App."

@app.route('/status')
def status():
    return jsonify ({"status": "OK", "service": "SRE Project App"})

@app.route('/error')
def error():
    response = make_response(jsonify({"error": "Internal Server Error"}), 500)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)