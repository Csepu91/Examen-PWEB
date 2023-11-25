from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ej1():
    if request.method == 'POST':
        v_nombre = request.form['nombre']
        v_edad = int(request.form['edad'])
        v_totpintura = round(float(9000 * int(request.form['cpintura'])),1)
        if 17 < v_edad < 31:
            return render_template('ejercicio1.html', r_nombre=f'Nombre del cliente: {v_nombre}', r_total=f'Total sin descuento: ${v_totpintura}', r_desc=f'El descuento es: ${round((v_totpintura*0.15),1)}',r_totald=f'El total a pagar es de: ${round((v_totpintura*0.85),1)}')
        elif v_edad > 30:
            return render_template('ejercicio1.html', r_nombre=f'Nombre del cliente: {v_nombre}', r_total=f'Total sin descuento: ${v_totpintura}', r_desc=f'El descuento es: ${round((v_totpintura*0.25),1)}', r_totald=f'El total a pagar es de: ${round((v_totpintura*0.75),1)}')
        else:
            return render_template('ejercicio1.html', r_nombre=f'Nombre del cliente: {v_nombre}', r_total=f'El total a pagar es de: ${v_totpintura}')
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ej2():
    if request.method == 'POST':
        user = request.form['usuario']
        contx = request.form['passw']
        dicc = {'juan': 'admin', 'pepe': 'user'}
        if user == "juan" and dicc[user] == contx:
            return render_template('ejercicio2.html', linex=f'Bienvenido administrador {user}')
        elif user == "pepe" and dicc[user] == contx:
            return render_template('ejercicio2.html', linex=f'Bienvenido usuario {user}')
        else:
            return render_template('ejercicio2.html', linex=f'Usuario o contraseña incorrectos')
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)