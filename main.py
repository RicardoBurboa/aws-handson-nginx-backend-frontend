from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(_name_)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="DATABASE-ENDPOINT",
        user="USERNAME",
        password="USER_PASSWORD",
        database="DATABASE_NAME"
    )

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tablename LIMIT 5;")
    usuarios = cursor.fetchall()
    conn.close()
    print(usuarios)


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
    

# If you want to test the "Hello World" from the API, uncomment the following code.
"""
from flask import Flask, jsonify
from flask_cors import CORS  # <--- IMPORTANTE

app = Flask(__name__)
CORS(app)  # <--- Habilita CORS para permitir peticiones desde el navegador

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hola Mundo desde la API privada'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
"""