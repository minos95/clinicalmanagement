from flask_wtf import FlaskForm
from wtforms import DateField,StringField, SubmitField,IntegerField
from wtforms.validators import  Length, DataRequired
class SurgeryForm(FlaskForm):
    name=StringField(label='Type dintervention', validators=[Length(min=2,max=30),DataRequired()])
    doctor=StringField(label='Operateur', validators=[Length(min=2,max=30), DataRequired()])
    anesthesist=StringField(label='anesthesist', validators=[Length(min=2,max=30), DataRequired()])
    date = DateField("La date de l'intervention", format='%d/%m/%Y')
    submit=SubmitField(label='Enregistrer')
    