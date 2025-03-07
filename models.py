from flask_sqlalchemy import SQLAlchemy
from app import app

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Modelo de la tabla productos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

# Crear la base de datos dentro del contexto de la aplicación
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Base de datos creada correctamente ✅")

