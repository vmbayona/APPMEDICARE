from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página "Quiénes Somos"
@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

# Ruta para la página de servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para la página de recursos
@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

# Ruta para la página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/consulta_gratis')
def consulta_gratis():
    return render_template('contacto.html')

@app.route('/buscar_especialistas')
def buscar_especialistas():
    return render_template('contacto.html')

@app.route('/servicio')
def servicio():
    return render_template('contacto.html')

@app.route('/enviar_contacto')
def enviar_contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
