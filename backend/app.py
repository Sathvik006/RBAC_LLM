# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from main_logic import load_and_add_data, generate_context, generate_response

app = Flask(__name__)
CORS(app) 

frontend_build_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'build'))

@app.route('/load_data', methods=['POST'])
def load_data():
    try:
        file = request.files['file']
        if file.filename == '':
            return jsonify({"status": "error", "message": "No file selected"}), 400
        
        file_path = os.path.join(frontend_build_dir, 'uploads', file.filename)
        file.save(file_path)
        
        load_and_add_data(file_path)
        
        return jsonify({"status": "success", "message": "File loaded successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

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

# Serve the React app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(frontend_build_dir, path)):
        return app.send_static_file(path)
    else:
        return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
