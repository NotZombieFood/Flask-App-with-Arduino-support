# coding=utf-8

from app import app
from flask import render_template, redirect, url_for, request, send_from_directory, request
import datetime, os


@app.route('/')
def base():
    return "test"

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

