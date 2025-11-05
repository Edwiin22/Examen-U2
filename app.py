from flask import Flask, request

app = Flask(__name__)

dispositivos = {}

@app.route('/dispositivos_mostrar', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
    <html>
    <head>
        <title>Dispositivos de red</title>
    </head>
    <body>
        <h2>Lista de dispositivos</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Descripción</th>
                    <th>IP</th>
                    <th>MAC</th>
                    <th>Ubicación</th>
                    <th>Tipo</th>
                    <th>Otros</th>
                </tr>
            </thead>
            <tbody>
    """
    for dispositivo_id, dispositivo in dispositivos.items():
        html += f"""
            <tr>
                <td>{dispositivo_id}</td>
                <td>{dispositivo['nombre']}</td>
                <td>{dispositivo['descripcion']}</td>
                <td>{dispositivo['ip']}</td>
                <td>{dispositivo['mac']}</td>
                <td>{dispositivo['ubicacion']}</td>
                <td>{dispositivo['tipo']}</td>
                <td>{dispositivo['otros']}</td>
            </tr>
        """
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivo():
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
def modificar_dispositivo(id):
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