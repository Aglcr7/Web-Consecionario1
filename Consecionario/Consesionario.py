from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Cargar autos desde archivo JSON
def cargar_autos():
    with open('database/autos.json') as f:
        return json.load(f)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ver lista de autos
@app.route('/autos')
def autos():
    lista_autos = cargar_autos()
    return render_template('autos.html', autos=lista_autos)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=8080)
