from flask import Flask
from data.data_productos import categorias, productos

app = Flask(__name__)


@app.route("/")
def home():
    return "<div><h1>Hola mi nombre es Alberto</h1><p>Soy de San Antonio Oeste, tengo, Rio Negro estoy cursando la Tecnicatura en Desarrollo Web 2025</p></div>"


@app.route("/categorias")
def listarCategorias():
    html = "<ul>"
    for cat in categorias:
        html += f"<li>{cat["id"]} {cat["descripcion"]}</li>"
    html += "</ul>"
    return html


@app.route("/productos")
def listarProductos():
    html = "<ul>"
    for prod in productos:
        html += f"<li>{prod["id"]} {prod["descripcion"]}</li>"
    html += "</ul>"
    return html


if __name__ == "__main__":
    app.run(debug=True)
