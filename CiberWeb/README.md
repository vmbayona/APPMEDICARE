Flask Application Documentation

This document provides a detailed explanation of the Flask application contained in `main.py`.

Overview

This is a simple Flask web application with several routes, each rendering a different HTML template. The application includes the following pages:
- Home
- Quiénes Somos (About Us)
- Services
- Resources
- Contact

Code Details

Imports

from flask import Flask, render_template

Flask: A class from the Flask framework used to create a Flask application instance.
render_template: A function used to render HTML templates.

Application Initialization

app = Flask(__name__)

Initializes a Flask application. `__name__` is passed to let Flask know where to look for resources such as templates and static files.

Route Definitions and Corresponding View Functions

Home Page Route

@app.route('/')
def index():
    return render_template('index.html')

Route: /
View Function: index
Template: index.html

Quiénes Somos Page Route

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

Route: /quienes_somos
View Function: quienes_somos
Template: quienes_somos.html

Services Page Route

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

Route: /servicios
View Function: servicios
Template: servicios.html

Resources Page Route

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

Route: /recursos
View Function: recursos
Template: recursos.html

Contact Page Route

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

Route: /contacto
View Function: contacto
Template: contacto.html

Running the Application

if __name__ == '__main__':
    app.run(debug=True)

This block ensures that the Flask application runs only if the script is executed directly (not imported as a module).
Debug Mode: `True` enables debug mode, providing detailed error pages and auto-restarting the server on code changes.

How to Run

1. Ensure you have Python and Flask installed.
2. Save the code in a file named `main.py`.
3. Run the application using the command:
   python main.py
4. Open a web browser and navigate to http://127.0.0.1:5000/ to view the application.

Templates

Make sure you have the following HTML templates in a `templates` directory:

- index.html
- quienes_somos.html
- servicios.html
- recursos.html
- contacto.html

Each template should be a valid HTML file corresponding to the respective route.

License

This project is licensed under the MIT License.
