# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from main_logic import load_and_add_data, generate_context, generate_response

app = Flask(__name__)
CORS(app) 



UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/load_data', methods=['POST'])
def load_data():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        load_and_add_data(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filepath': filepath}), 200

    return jsonify({'message': 'Invalid file type'}), 400
        
        
        
@app.route('/query', methods=['POST'])
def query():
    try:
        user = request.json['user']
        query = request.json['query']
        context = generate_context(user, query)
        answer = generate_response(context, query)
        return jsonify({"status": "success", "answer": answer}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
