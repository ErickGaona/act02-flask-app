from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # URL del archivo de datos
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"

    # Leer el contenido del archivo desde internet
    respuesta = requests.get(url)
    texto = respuesta.text

    # Dividir el texto por líneas
    lineas = texto.strip().split('\n')

    # Lista para guardar personas filtradas
    personas_filtradas = []

    # Revisar cada línea
    for linea in lineas:
        datos = linea.split(";")  # Separar los campos por ";"
        id_persona = datos[0]
        
        # Filtrar si el ID comienza con 3, 4, 5 o 7
        if id_persona[0] in ['3', '4', '5', '7']:
            personas_filtradas.append(datos)

    # Enviar la lista a una plantilla HTML
    return render_template("tabla.html", personas=personas_filtradas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)