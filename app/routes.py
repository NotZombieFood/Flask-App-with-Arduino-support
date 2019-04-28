# coding=utf-8
# cd Documents/LDI/Flask-App-with-Arduino-support
from app import app
from flask import render_template, redirect, url_for, request, send_from_directory, request
import datetime, os, threading, serial, time


global lista_valores

lista_valores = []
arduino = serial.Serial("COM3",9600,timeout = 2)
# arduino.close()
def checkVal():    
    rawString = arduino.readline()
    value = rawString.decode("utf-8").replace("\r","").replace("\n","")
    return value

def append(value):
    lista_valores.append(value)

def f(f_stop):
    valor = checkVal()
    if valor != '':
        if int(valor)>50:
            append(int(valor))
    if not f_stop.is_set():
        # call f() again in 60 seconds
        threading.Timer(.5, f, [f_stop]).start()

f_stop = threading.Event()
# start calling f now and every 60 sec thereafter
f(f_stop)

@app.route('/')
def base():
    return "test"

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

@app.route('/monitor')
def loadMonitor():
    return render_template('monitor.html', value = lista_valores[-1])

@app.route('/graph')
def loadGraph():
    return render_template('grapher.html', list = lista_valores)

@app.route('/latest')
def getLatestValue():
    return str(lista_valores[-1])


@app.route('/values')
def getValues():
    return str(lista_valores)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

