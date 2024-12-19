from flask import Flask, render_template, jsonify
import random
import json
import os

app = Flask(__name__)

# Load the JSON data from the file
def load_qian_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, 'qian.json')
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_qian_name():
    # Load the data dynamically
    data = load_qian_data()
    pick = str(random.randint(1, 100))
    c = data['灵签诗文'][pick]
    result = {
        "qian_name": data['qian_name'][pick],
        "content": "<br>".join([c[i*7:(i+1)*7] for i in range(4)]),
        "type": data['吉凶'][pick],
        "meaning": data['诗意'][pick],
        "raw_explaination": data['解曰'][pick],
        "high_level_explaination": data['整体解释'][pick],
        "job_explaination": data['解曰'][pick],
        "love_explaination": data['解曰'][pick],
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)