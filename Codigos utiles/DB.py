import pyodbc

# Configuración de la conexión
server = 'DESKTOP-NJ31F30'  # Nombre del servidor
database = 'Medical_Startup'  # Nombre de la base de datos
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'Trusted_Connection=yes;'
)

# Conectar a la base de datos
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute('SELECT * FROM nueva_tabla')  # Reemplaza "nombre_tabla" con el nombre de tu tabla

# Obtener los resultados
rows = cursor.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)

# Cerrar la conexión
cursor.close()
conn.close()
