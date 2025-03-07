# Importamos Flask
from flask import Flask  

# Creamos una instancia de Flask
app = Flask(__name__)  

# Definimos la ruta principal "/"
@app.route('/')
def home():
    return "¡Bienvenido al Sistema de Inventario de Restaurante!"

# Ejecutamos la aplicación si este archivo es el principal
if __name__ == "__main__":
    app.run(debug=True)
