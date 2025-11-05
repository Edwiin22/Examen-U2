from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

dispositivos = {}

@app.route('/dispositivo', methods=['GET'])
def mostrar_dispositivo():
    html = """
    <html>
     <head>
    <tittle> Dispositivos </tittle>
    <style> .dispositivo
    border: 2px;
    header: 10px;
    backgroun-color: #222222
    </style>
     </head>

     <body>
     <h1> Lista de Dispositivos </h1>
     <p>ID: </P>
     </br>
     <p>Nombre: </p>
    <p>descripcion:</P>
    <p> IP: </P>
    <p> MAC: </p>
    <p> Ubicacion: </p>
    <p> Tipo: </p>
    <p> Otros: </p>
    </html>
    """

for dispositivoID in dispositivos():
    html += f"""
<p>{dispositivos.get(id)}</p>
<p>{dispositivos.get(Nombre)}</P>
<P>{dispositivos.get(descripcion)}</p>
<p>{dispositivos.get(IP)}</P>
<p>{dispositivos.get(Mac)}</p>
<p>{dispositivos.get(Ubicacion)}</p>
<p>{dispositivos.get(Tipo)}</p>
<p>{dispositivos.get(otros)}</p>
"""
   

@app.route('/dispositivos', methods=['POST'])
def agregar_Dispositivo():
    data = request.get_json()
    dispositivoID = data.get('id')
    if dispositivoID in dispositivos:
        return jsonify