#muestra plantillas render_template
from flask import render_template
from . import products

@products.route('/create')
def crear_productos():
    return render_template('new.html')
