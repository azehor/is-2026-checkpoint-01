import os
import psycopg2

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


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


#Endpoint para la lista de miembros de la BD

@app.route('/api/team', methods=['GET'])
def get_team():
    try:
        connection = db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT nombre, apellido, legajo, feature, estado, servicio FROM members;')
        bd_response = cursor.fetchall()

        team = [
                {"nombre": member[0], "apellido": member[1], "legajo": member[2], "feature": member[3], "estado": member[4], "servicio": member[5]}
            for member in bd_response
        ]

        cursor.close()
        connection.close()
        
        response = jsonify(team)

        return response, 200

    except Exception as error:
        response = jsonify({
            "error": "Error de conexion a la base de datos",
            "details": str(error)
        })
        return response, 500



if __name__ == '__main__':
    #La api escucha el puerto 5000
    app.run(host='0.0.0.0', port=5000)
