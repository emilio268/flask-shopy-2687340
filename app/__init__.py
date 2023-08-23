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

#dependencia a bootstrap 
from flask_bootstrap import Bootstrap

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

#creaar objeto bootstrap
bootstrap = Bootstrap(app)

#importar los modelos de .models

from .models import Cliente, Producto, Venta, Detalle


