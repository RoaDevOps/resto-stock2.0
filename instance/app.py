from models import db, Producto  # Importar la base de datos y el modelo de Producto

# Crear algunos productos de ejemplo
with app.app_context():
    # Asegurarse de que la base de datos esté vacía antes de agregar datos
    db.drop_all()  # Elimina las tablas (solo para pruebas, lo puedes eliminar después)
    db.create_all()  # Crea las tablas

    # Agregar productos de ejemplo
    producto1 = Producto(nombre='Hamburguesa', descripcion='Deliciosa hamburguesa de carne', cantidad=50, precio=5.99)
    producto2 = Producto(nombre='Papas Fritas', descripcion='Papas fritas crujientes', cantidad=100, precio=2.99)
    producto3 = Producto(nombre='Soda', descripcion='Refresco refrescante', cantidad=200, precio=1.50)

    # Agregar productos a la base de datos
    db.session.add_all([producto1, producto2, producto3])
    db.session.commit()

    print("Productos de ejemplo insertados correctamente ✅")
