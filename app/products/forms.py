from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


#Formulario de registro de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField("inrese nombre:")
    precio = StringField("inrese precio:")
    submit = SubmitField("Registre producto")