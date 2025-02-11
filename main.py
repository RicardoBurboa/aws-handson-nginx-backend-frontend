from flask import Flask, jsonify
from flask_cors import CORS  # <--- IMPORTANTE

app = Flask(__name__)
CORS(app)  # <--- Habilita CORS para permitir peticiones desde el navegador

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hola Mundo desde la API privada'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)