from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import random
from flask import Flask, request, jsonify
import pyodbc


app = Flask(__name__)

# Configuración de la conexión
server = 'DESKTOP-NJ31F30'  # Nombre del servidor
database = 'Medical_Startup'  # Nombre de la base de datos
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'Trusted_Connection=yes;'
)

# Rutas para las diferentes páginas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')



@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/consulta_gratis')
def consulta_gratis():
    return render_template('contacto.html')

@app.route('/buscar_especialistas')
def buscar_especialistas():
    return render_template('especialistas.html')

@app.route('/servicio')
def servicio():
    return render_template('contacto.html')

@app.route('/enviar_contacto')
def enviar_contacto():
    return render_template('contacto.html')









@app.route('/registrate_paciente', methods=['GET','POST'])
def registrate_paciente():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    celular = request.form.get('celular')
    correo = request.form.get('correo')
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    genero = request.form.get('genero')
    direccion = request.form.get('direccion')
    ubicacion = request.form.get('ubicacion')  # Asegúrate de obtener la ubicación del formulario

    # Verificar si las contraseñas coinciden
    if password != confirm_password:
        error = "Las contraseñas no coinciden"
        return render_template('registrate_paciente.html', error=error)

    # Conectar a la base de datos
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    try:
        # Insertar datos en la tabla
        cursor.execute('''
            INSERT INTO Pacientes (Nombre, Apellido, Celular, Correo, Usuario, Password, FechaNacimiento, Genero, Direccion, Ubicacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, celular, correo, usuario, password, fecha_nacimiento, genero, direccion, ubicacion))

        # Confirmar los cambios
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

        # Renderizar la plantilla de registro exitoso
        return render_template('registro_exitoso.html', nombre=nombre)
    except pyodbc.Error as e:
        error_message = str(e)
        # Manejar el error aquí (puede imprimirse o renderizarse en la plantilla)
        return render_template('registrate_paciente.html', error=error_message)




@app.route('/registrate_medico', methods=['GET', 'POST'])
def registrate_medico():
    if request.method == 'POST':
        # Aquí procesas los datos del formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        celular = request.form.get('celular')
        correo = request.form.get('correo')
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            error = "Las contraseñas no coinciden"
            return render_template('registrate_medico.html', error=error)

        # Aquí podrías guardar los datos en la base de datos o hacer cualquier otra acción necesaria
        
        # Renderizas la plantilla con un mensaje de registro exitoso
        return render_template('registro_exitoso.html', nombre=nombre)
    return render_template('registrate_medico.html')

@app.route('/login_usuario')
def login_usuario():
    return render_template('login_medico.html')




# Función para verificar las credenciales del paciente
def verificar_credenciales(usuario, password):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Consultar si existe un usuario con las credenciales proporcionadas
    cursor.execute('SELECT COUNT(*) FROM Pacientes WHERE Usuario = ? AND Password = ?', (usuario, password))
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count > 0

@app.route('/login_paciente', methods=['GET', 'POST'])
def login_paciente():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        # Verificar credenciales
        if verificar_credenciales(usuario, password):
            # Las credenciales son válidas, redirigir a una página de inicio de sesión exitosa
            return redirect(url_for('inicio_exitoso', usuario=usuario))
        else:
            error = "Usuario o contraseña incorrectos"
            return render_template('login_paciente.html', error=error)

    return render_template('login_paciente.html')

@app.route('/<usuario>')
def inicio_exitoso(usuario):
    return render_template('inicio_exitoso.html', usuario=usuario)


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


if __name__ == '__main__':
    app.run(debug=True)
