#dependencia flask 
from flask import Flask

#dependencia de configuración con (.) para llamarlo
from .config import Config

#dependencias de modelos 
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones 
from flask_migrate import Migrate

from .mi_blueprint import mi_blueprint
from app.products import products


#crear el objeto flask 
app = Flask(__name__)

#configuración del objeto flask
app.config.from_object(Config)

#Vincular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)


#Crear el objeto de Modelos
db = SQLAlchemy(app)

#Crear objeto de Migración
migrate = Migrate(app, db)

#importar los modelos de .models

from .models import Cliente, Producto, Venta, Detalle


