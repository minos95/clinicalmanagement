from flask_wtf import FlaskForm
from wtforms import DateField,StringField, SubmitField,IntegerField
from wtforms.validators import  Length, DataRequired
class DoctorForm(FlaskForm):
    firstname=StringField(label='fisrtname', validators=[Length(min=2,max=30),DataRequired()])
    lastname=StringField(label='Lastname', validators=[Length(min=2,max=30),DataRequired()])
    speciality=StringField(label='specialty', validators=[Length(min=2,max=30),DataRequired()])
    submit=SubmitField(label='Enregistrer')
    