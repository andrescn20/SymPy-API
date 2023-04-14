from flask import Flask , request , jsonify
from flask_cors import CORS
from functions import *

app = Flask(__name__)
CORS(app)
    
@app.route('/')
def home():
        return jsonify({'response' : 'Connection Successful'})


@app.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return jsonify({"response": "Get Request"})


@app.route('/Sumar', methods=['POST'])
def call_suma(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Sumar(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Restar', methods=['POST'])
def call_resta(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Restar(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Multiplicar', methods=['POST'])
def call_multiplicar(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Multiplicar(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Dividir', methods=['POST'])
def call_dividir(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Dividir(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Potencia', methods=['POST'])
def call_potencia(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Potencia(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Raiz', methods=['POST'])
def call_raiz(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Raiz(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Simplificar', methods=['POST'])
def call_simplificar(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Simplificar(data['equation'], data['factor']) 
        return jsonify(result) 
    

@app.route('/Expandir', methods=['POST'])
def call_expandir(): 
    if request.method == 'POST': 
        data = request.get_json() 
        result = Expandir(data['equation'], data['factor']) 
        return jsonify(result) 

    
