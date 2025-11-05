from flask import Flask, request

app = Flask(__name__)

dispositivos = {}

@app.route('/dispositivos', methods=['GET'])
def mostrar_dispositivos():
    html = """
    <html>
    <head>
        <title>Dispositivos de red</title>
    </head>
    <body>
        <h2>Lista de dispositivos</h2>
        
            
                    <p>ID</p>
                    <p>Nombre</p>
                    <p>Descripción</p>
                    <p>IP</p>
                    <p>MAC</p>
                    <p>Ubicación</p>
                    <p>Tipo</p>
                    <p>Otros</p>
                
            </body>
    """
    for dispositivo_id, dispositivo in dispositivos.items():
        html += f"""
            
                <p>{dispositivo_id}</p>
                <p>{dispositivo['nombre']}</p>
                <p>{dispositivo['descripcion']}</p>
                <p>{dispositivo['ip']}</p>
                <p>{dispositivo['mac']}</p>
                <p>{dispositivo['ubicacion']}</p>
                <p>{dispositivo['tipo']}</p>
                <p>{dispositivo['otros']}</p>
            
        """
        return {"mensaje: vacio"}
   

@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivos():
    nuevo = request.get_json()
    dispositivos[nuevo['id']] = {
        'nombre': nuevo['nombre'],
        'descripcion': nuevo['descripcion'],
        'ip': nuevo['ip'],
        'mac': nuevo['mac'],
        'ubicacion': nuevo['ubicacion'],
        'tipo': nuevo['tipo'],
        'otros': nuevo.get('otros', '')
    }
    return {"mensaje": "Dispositivo agregado correctamente"}, 201

@app.route('/dispositivos/<id>', methods=['PUT'])
def modificar_dispositivos(id):
    if id not in dispositivos:
        return {"error": "No encontrado"}, 404
    datos = request.get_json()
    dispositivos[id].update({
        'nombre': datos.get('nombre', dispositivos[id]['nombre']),
        'descripcion': datos.get('descripcion', dispositivos[id]['descripcion']),
        'ip': datos.get('ip', dispositivos[id]['ip']),
        'mac': datos.get('mac', dispositivos[id]['mac']),
        'ubicacion': datos.get('ubicacion', dispositivos[id]['ubicacion']),
        'tipo': datos.get('tipo', dispositivos[id]['tipo']),
        'otros': datos.get('otros', dispositivos[id]['otros'])
    })
    return {"mensaje": "Dispositivo actualizado correctamente"}

if __name__ == '__main__':
    app.run(debug=True)