from distutils.log import error
from unicodedata import name
from flask import Flask, render_template, request
from CLASES.cuentas_usuario import *
from datetime import date
import os
import urllib.parse
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/login')
def inicio():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/menu-r')
def menu_r():
    return render_template('menu_rodilla.html',usuario=usuario,dia=dia)

@app.route('/menu-t')
def menu_t():
    return render_template('menu_tobillo.html',usuario=usuario,dia=dia)

@app.route('/menu-m')
def menu_m():
    return render_template('menu_muneca.html',usuario=usuario,dia=dia)

@app.route('/recu_dia1m')
def recu_dia1m():
    return render_template('recu_dia1m.html', usuario=usuario)

@app.route('/recu_dia2m')
def recu_dia2m():
    return render_template('recu_dia2m.html',usuario=usuario)

@app.route('/recu_dia3m')
def recu_dia3m():
    return render_template('recu_dia3m.html',usuario=usuario)

@app.route('/recu_dia4m')
def recu_dia4m():
    return render_template('recu_dia4m.html',usuario=usuario)

@app.route('/recu_dia5m')
def recu_dia5m():
    return render_template('recu_dia5m.html',usuario=usuario)

@app.route('/recu_dia6m')
def recu_dia6m():
    return render_template('recu_dia6m.html',usuario=usuario)

@app.route('/recu_dia7m')
def recu_dia7m():
    return render_template('recu_dia7m.html',usuario=usuario)

@app.route('/recu_dia1r')
def recu_dia1r():
    return render_template('recu_dia1r.html',usuario=usuario)

@app.route('/recu_dia2r')
def recu_dia2r():
    return render_template('recu_dia2r.html',usuario=usuario)

@app.route('/recu_dia3r')
def recu_dia3r():
    return render_template('recu_dia3r.html',usuario=usuario)

@app.route('/recu_dia4r')
def recu_dia4r():
    return render_template('recu_dia4r.html',usuario=usuario)

@app.route('/recu_dia5r')
def recu_dia5r():
    return render_template('recu_dia5r.html',usuario=usuario)

@app.route('/recu_dia6r')
def recu_dia6r():
    return render_template('recu_dia6r.html',usuario=usuario)

@app.route('/recu_dia7r')
def recu_dia7r():
    return render_template('recu_dia7r.html',usuario=usuario)

@app.route('/sube_dia1m')
def sube_dia1m():
    return render_template('sube_dia1m.html',usuario=usuario)

@app.route('/sube_dia2m')
def sube_dia2m():
    return render_template('sube_dia2m.html',usuario=usuario)

@app.route('/sube_dia3m')
def sube_dia3m():
    return render_template('sube_dia3m.html',usuario=usuario)

@app.route('/sube_dia4m')
def sube_dia4m():
    return render_template('sube_dia4m.html',usuario=usuario)

@app.route('/sube_dia5m')
def sube_dia5m():
    return render_template('sube_dia5m.html',usuario=usuario)

@app.route('/sube_dia6m')
def sube_dia6m():
    return render_template('sube_dia6m.html',usuario=usuario)

@app.route('/sube_dia7m')
def sube_dia7m():
    return render_template('sube_dia7m.html',usuario=usuario)

@app.route('/sube_dia1t')
def sube_dia1t():
    return render_template('sube_dia1t.html',usuario=usuario)

@app.route('/sube_dia2t')
def sube_dia2t():
    return render_template('sube_dia2t.html',usuario=usuario)

@app.route('/sube_dia3t')
def sube_dia3t():
    return render_template('sube_dia3t.html',usuario=usuario)

@app.route('/sube_dia4t')
def sube_dia4t():
    return render_template('sube_dia4t.html',usuario=usuario)

@app.route('/sube_dia5t')
def sube_dia5t():
    return render_template('sube_dia5t.html',usuario=usuario)

@app.route('/sube_dia6t')
def sube_dia6t():
    return render_template('sube_dia6t.html',usuario=usuario)

@app.route('/sube_dia7t')
def sube_dia7t():
    return render_template('sube_dia7t.html',usuario=usuario)

@app.route('/sube_dia1r')
def sube_dia1r():
    return render_template('sube_dia1r.html',usuario=usuario)

@app.route('/sube_dia2r')
def sube_dia2r():
    return render_template('sube_dia2r.html',usuario=usuario)

@app.route('/sube_dia3r')
def sube_dia3r():
    return render_template('sube_dia3r.html',usuario=usuario)

@app.route('/sube_dia4r')
def sube_dia4r():
    return render_template('sube_dia4r.html',usuario=usuario)

@app.route('/sube_dia5r')
def sube_dia5r():
    return render_template('sube_dia5r.html',usuario=usuario)

@app.route('/sube_dia6r')
def sube_dia6r():
    return render_template('sube_dia6r.html',usuario=usuario)

@app.route('/sube_dia7r')
def sube_dia7r():
    return render_template('sube_dia7r.html',usuario=usuario)

@app.route('/recu_dia1t')
def recu_dia1t():
    return render_template('recu_dia1t.html',usuario=usuario)

@app.route('/recu_dia2t')
def recu_dia2t():
    return render_template('recu_dia2t.html',usuario=usuario)

@app.route('/recu_dia3t')
def recu_dia3t():
    return render_template('recu_dia3t.html',usuario=usuario)

@app.route('/recu_dia4t')
def recu_dia4t():
    return render_template('recu_dia4t.html',usuario=usuario)

@app.route('/recu_dia5t')
def recu_dia5t():
    return render_template('recu_dia5t.html',usuario=usuario)

@app.route('/recu_dia6t')
def recu_dia6t():
    return render_template('recu_dia6t.html',usuario=usuario)

@app.route('/recu_dia7t')
def recu_dia7t():
    return render_template('recu_dia7t.html',usuario=usuario)

@app.route('/contacto_t')
def contacto_t():
    return render_template('contacto_t.html', usuario=usuario)

@app.route('/contacto_m')
def contacto_m():
    return render_template('contacto_m.html', usuario=usuario)

@app.route('/contacto_r')
def contacto_r():
    return render_template('contacto_r.html', usuario=usuario)

@app.route('/registrar', methods = ["POST"])
def registrar():
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']
        correo = request.form['correo']
        lesion = request.form['lesion']
        grado = request.form['grado']
        print(usuario)
        print(password)
        print(lesion)
        print(grado)
        registrado = menu_registro(usuario,password,correo,lesion,grado)
        if registrado == "1":
            return render_template('login.html')
        if registrado == "0":
            mensaje = "Ya existe ese usuario, por favor inserte otro"
            return render_template('register.html', mensaje= mensaje)

@app.route('/validar', methods = ["POST"])
def validar():
    global usuario, dia
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario)
        print(password)
        t = menu_validacion(usuario,password)
        if t == "1":
            tipo = tipo_menu(usuario,password)
            dia = tipo_dia(usuario,password)
            grado = tipo_grado(usuario,password)
            if tipo == "Rodilla":
                if grado == "Grado 1":
                    return render_template('menu_rodilla.html', usuario=usuario, dia = dia)
                if grado == "Grado 2":
                    return render_template('menu_rodilla.html', usuario=usuario, dia = dia)
                if grado == "Grado 3":
                    return render_template('menu_rodilla.html', usuario=usuario, dia = dia)

            if tipo == "Tobillo":
                if grado == "Grado 1":
                    return render_template('menu_tobillo.html', usuario=usuario, dia = dia)
                if grado == "Grado 2":
                    return render_template('menu_tobillo.html', usuario=usuario, dia = dia)
                if grado == "Grado 3":
                    return render_template('menu_tobillo.html', usuario=usuario, dia = dia)
                
            if tipo == "Muneca":
                if grado == "Grado 1":
                    return render_template('menu_muneca.html', usuario=usuario, dia= dia)
                if grado == "Grado 2":
                    return render_template('menu_muneca.html', usuario=usuario, dia= dia)
                if grado == "Grado 3":
                    return render_template('menu_muneca.html', usuario=usuario, dia= dia)
                
        else:
            return render_template('login.html', err= "ERROR!!", avis="Datos incorrectos!")
        

@app.route("/uploadm", methods=['POST'])
def uploader3():
    app.config['UPLOAD_FOLDER1'] = './Archivos/Muñeca'+"/"+usuario
    if request.method == 'POST':
    # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER1'], filename))
        # Retornamos una respuesta satisfactoria
        mensaje = "Archivo subido exitosamente"
        return render_template('menu_muneca.html', usuario = usuario, dia = dia, mensaje = mensaje)

@app.route("/uploadt", methods=['POST'])
def uploader2():
    app.config['UPLOAD_FOLDER2'] = './Archivos/Tobillo'+"/"+usuario
    if request.method == 'POST':
    # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename))
        # Retornamos una respuesta satisfactoria
        mensaje = "Archivo subido exitosamente"
        return render_template('menu_tobillo.html', usuario = usuario, dia = dia, mensaje = mensaje)

@app.route("/uploadr", methods=['POST'])
def uploader1():
    app.config['UPLOAD_FOLDER3'] = './Archivos/Rodilla'+"/"+usuario
    if request.method == 'POST':
    # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER3'], filename))
        # Retornamos una respuesta satisfactoria
        mensaje = "Archivo subido exitosamente"
        return render_template('menu_rodilla.html', usuario = usuario, dia = dia, mensaje = mensaje)

if __name__ == "__main__":
    app.run(debug=True)