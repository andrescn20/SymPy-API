from flask import Flask, request, jsonify
from main import * #Importamos todas las funciones del main para poder accesarlas

app = Flask(__name__)


@app.route("/test")
def test():
    return {'test': 'Hola Jose :3'}

#define el método por el que se envía el request (post)
@app.route('/Sumar', methods=['POST'])
def call_suma(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Sumar(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Restar', methods=['POST'])
def call_resta(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Restar(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Multiplicar', methods=['POST'])
def call_multiplicar(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Multiplicar(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Dividir', methods=['POST'])
def call_dividir(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Dividir(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Potencia', methods=['POST'])
def call_potencia(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Potencia(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Raiz', methods=['POST'])
def call_raiz(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Raiz(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json

    
#define el método por el que se envía el request (post)
@app.route('/Simplificar', methods=['POST'])
def call_simplificar(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Simplificar(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json
    
#define el método por el que se envía el request (post)
@app.route('/Expandir', methods=['POST'])
def call_expandir(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = Expandir(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json

#define el método por el que se envía el request (post)
@app.route('/Expandir', methods=['POST'])
def call_latex(): #nombre de la función
    if request.method == 'POST': #verificamos que el método que viene del FE es el correcto
        data = request.get_json() #El request es un archivo grande, esto toma la parte que nos interesa
        result = getLatex(data['equation'], data['factor']) #Enviamos nuestros parámetros a la función. Ojo que tienen que coincidir con lo que viene de FE. 
        response = {'result': result} # Generamos el objeto que vamos a devolver
        return jsonify(response) #Enviamos la respuesta en Formato Json






if __name__ == "__main__":
    app.run(debug=True)
