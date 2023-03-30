from flask import Flask, request, jsonify
from main import * #Importamos todas las funciones del main para poder accesarlas

app = Flask(__name__)


@app.route("/test")
def test():
    return {'test': 'Hola Jose :3'}

#define el método por el que se envía el request (post)
@app.route('/suma', methods=['POST'])
def call_suma(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = suma(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json


if __name__ == "__main__":
    app.run(debug=True)