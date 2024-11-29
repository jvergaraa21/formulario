from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def formulario():
    # Carga el formulario HTML
    with open('formulario.html', 'r', encoding='utf-8') as file:
        html = file.read()
    return html

@app.route('/guardar', methods=['POST'])
def guardar():
    # Obtiene los datos del formulario
    carrera = request.form['carrera']
    primer_nombre = request.form['primer_nombre']
    correo = request.form['correo']

    # Formatea los datos
    datos = f"Carrera: {carrera}\nPrimer nombre: {primer_nombre}\nCorreo: {correo}\n{'-'*40}\n"

    # Guarda los datos en un archivo de texto
    with open('datos.txt', 'a', encoding='utf-8') as file:
        file.write(datos)

    return f"""
    <h1>¡Gracias por registrarte!</h1>
    <p>Tu información ha sido guardada exitosamente.</p>
    <a href="/">Volver al formulario</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
