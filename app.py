from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient('mongodb://172.31.86.5:27017/')
db = client['mi_base_de_datos']
collection = db['usuarios']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        edad = request.form['edad']

        # Insertar los datos en MongoDB
        usuario = {
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
            'direccion': direccion,
            'edad': edad
        }
        collection.insert_one(usuario)

        return redirect('/')

