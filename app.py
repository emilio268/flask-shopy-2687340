#dependencia flask 

from flask import Flask, render_template
# dependencias de modelos 

from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones 
from flask_migrate import Migrate

#dependencia para fecha y hora del sistema 
from datetime import datetime

#dependencias de wtform
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#crear el objeto flask 
app = Flask(__name__)

#definir la cadena de conexión (connectionstring)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3311/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'Danaiko'

#Crear el objeto de Modelos

db = SQLAlchemy(app)

#Crear objeto de Migración

migrate = Migrate(app, db)

#Crear Formulario de registro de productos

class ProductosForm(FlaskForm):
    nombre = StringField('Ingrese un nombre para el producto')
    precio = StringField('Ingrese un precio para el producto')
    submit = SubmitField('Registrar Producto')

#Crear los modelos:
class Cliente(db.Model):
    #Definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(128), nullable = True)
    email = db.Column(db.String(128), nullable = True)
    
#relacines SQL alchemy

    ventas = db.relationship('Venta', 
                             backref = "cliente",
                             lazy = "dynamic")

    
class Producto(db.Model):
    #Definir los Atributos
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))


class Venta (db.Model):
    #definir los atributos
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, 
                      default = datetime.utcnow)
    
    #Clave foránea:
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))
    
class Detalle (db.Model):
     #definir los atributos
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer)
    
#clave foránea

    producto_id = db.Column(db.Integer, 
                           db.ForeignKey('productos.id'))
    
    venta_id = db.Column(db.Integer, 
                           db.ForeignKey('ventas.id'))    
    
    #Rutas: 
@app.route('/productos', methods = ['GET', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
        #Creamos un nuevo producto
        p = Producto(nombre = form.nombre.data, 
                     precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "produto Registrado" 
    
    return render_template('nuevo_producto.html',
                    form = form)
    