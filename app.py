from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/promociones')
def promociones():
    return render_template('promociones.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)