#dependencia flask 
from flask import Flask

#dependencia de configuración con (.) para llamarlo
from .config import Config

#dependencias de modelos 
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones 
from flask_migrate import Migrate


#crear el objeto flask 
app = Flask(__name__)

#configuración del objeto flask
app.config.from_object(Config)


#Crear el objeto de Modelos
db = SQLAlchemy(app)

#Crear objeto de Migración
migrate = Migrate(app, db)

#importar los modelos de .models

from .models import Cliente, Producto, Venta, Detalle


