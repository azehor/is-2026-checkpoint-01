import os
import psycopg2

from flask import Flask, jsonify


app = Flask(__name__)


#Variables de entorno

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


#Coneccion con la BD

def db_connection():
    return psycopg2.connect(
        host = DB_HOST,
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD
    )


#Endpoint para el HEALTHCHECK

@app.route('/api/health', methods=['GET'])
def health():
    response = jsonify({"status": "active"})
    return response, 200


#Endpoint para la metada
@app.route('/api/info', methods=['GET'])
def info():
    response = jsonify({
        "service": "backend-api",
        "tech": "Python 3.12-slim + Flask",
        "feature": "03 - Backend Implementation"
    })
    return response, 200


if __name__ == '__main__':
    #La api escucha el puerto 5000
    app.run(host='0.0.0.0', port=5000)
