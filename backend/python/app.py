from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    # Implement character generation logic here
    character = generate_character(data) # replace with logic
    return jsonify({"character": character})

def generate_character(data):
    # placeholder for actual character generation
    return "Python-generated character"

if __name__ == '__main__':
    app.run(port=5001)