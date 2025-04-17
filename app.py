from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"

    
    respuesta = requests.get(url)
    texto = respuesta.text

    lineas = texto.strip().split('\n')

    personas = []

    for linea in lineas:
        datos = linea.split(";")  
        id_persona = datos[0]
        if id_persona[0] in ['3', '4', '5', '7']:  
            personas.append(datos)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Personas filtradas</title>
    </head>
    <body>
        <h1>Personas con ID que comienza en 3, 4, 5 o 7</h1>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Edad</th>
                <th>Correo</th>
            </tr>
            {% for persona in personas %}
            <tr>
                <td>{{ persona[0] }}</td>
                <td>{{ persona[1] }}</td>
                <td>{{ persona[2] }}</td>
                <td>{{ persona[3] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    return render_template_string(html, personas=personas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)