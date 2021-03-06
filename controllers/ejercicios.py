from flask import Flask , Blueprint, render_template, request, redirect, url_for, send_file, after_this_request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import Required

import subprocess
from subprocess import PIPE
from entities.Ejercicio import Ejercicio
import os, uuid, re, tempfile
import time
import re

form_blueprint = Blueprint('form', __name__)

# CONSOLA PARA EJERCITAR
@form_blueprint.route('/form', methods = ['POST', 'GET'])
@form_blueprint.route('/form/<seccion>/<tema>/<string:ej>', methods = ['POST', 'GET'])
def form(seccion, tema, ej):
    form = CodeForm(request.form)
    result = ""
    pruebas = ej
    if not form.editor.data:
        form.editor.data = formato_funcion(tema, pruebas)

    lista_ejs = ordenar_lista_directorio(os.listdir("templates/ejercicios/{}/{}".format(seccion,tema)))
    prox_ej = getProximoEjercicio(seccion,tema, ej)

    ejercicio = Ejercicio(tema, ej, seccion)

    if request.method == 'POST' and form.validate():
        ejercicio.mostrar_consola()
        if request.form['submit'] == 'Print':
            filename = str(uuid.uuid4().hex) + '.py'
            with open(filename,'w') as file:
                file.write(form.editor.data)
            # Remuevo el archivo creado para descargar el código
            @after_this_request 
            def remove_file(response): 
                os.remove(filename) 
                return response 

            return send_file(filename,  attachment_filename = ej + '.py', as_attachment=True)
        ejercicio.setear_resultado(str(runCode(form.editor.data, tema, pruebas)))
    return render_template('ejercicios.html', prox_ej = prox_ej, 
                            form = form, ejercicio = ejercicio, ejs_tema = len(lista_ejs))


class CodeForm(Form):
    editor = TextAreaField('editor')
    submit = SubmitField('Submit')

def runCode(code, tema, pruebas_ej):
    pruebas = ''
    with open(f'pruebas/{tema}/{pruebas_ej}.py') as test:
        pruebas = test.read()

    base_name = str(uuid.uuid4().hex)
    filename = base_name + '.py'
    folder_name = base_name

    # Create user folder
    os.mkdir(f"./{folder_name}")

    # Create the untrusted code file
    with open(f"./{folder_name}/{filename}",'w') as file:
        file.write('import unittest' + '\n' + code + '\n\n' + pruebas)

    # Command to execute
    command = (f"docker run "
                f"-v {os.getcwd()}/{folder_name}:/src"
                f" --attach STDOUT --attach STDERR "
                f" run-container python3 ./{filename} -v").split()

    # Excecute the untrusted code
    proc = subprocess.Popen(command,stdout=PIPE, stderr=PIPE)
    try:
        outs, errs = proc.communicate(timeout=10)
        errs = errs.decode('UTF-8')
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        errs = 'TimeoutExpires exception'

    # Remove the user folder and container
    command = f"rm -rf ./{folder_name}".split()
    subprocess.Popen(command) #Python remove dir does not allow remove a non empty folder

    command = f"./CleanContainers.sh".split()
    subprocess.Popen(command)

    return errs

def formato_funcion(tema, pruebas_ej):
    with open(f"pruebas/{tema}/{pruebas_ej}.py") as pruebas:
        nombre_funcion = pruebas.readline()
        regex = re.compile('#\s*')
        return regex.sub('',nombre_funcion).rstrip() 

def ordenar_lista_directorio(lista):
    return sorted(lista, key = lambda nombre: nombre[0])

def getProximoEjercicio(seccion, tema, ej):
    #Refactorizar, lo hago rápido
    list_ejs = []
    num_ej = 0
    with open(f"info/{seccion}/{tema}.csv") as seccion:
        for i,ejercicio in enumerate(seccion):
            list_ejs.append(ejercicio)
            if ejercicio.rstrip('\n') == ej:
                num_ej = i
    return list_ejs[ (num_ej + 1) % len(list_ejs)].rstrip('\n')

