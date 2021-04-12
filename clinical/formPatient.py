from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,DateField,validators
from wtforms.validators import  Length, DataRequired 

class RegisterForm(FlaskForm):
    lastname=StringField(label='Nom', validators=[Length(min=2,max=30),DataRequired()])
    firstname=StringField(label='Prenom', validators=[Length(min=2,max=30), DataRequired()])
    age=IntegerField(label='Age', validators=[ DataRequired()])
    address=StringField(label='Address')
    phone=StringField(label='Telephone')
    identity=IntegerField(label='Num Identite', validators=[ DataRequired()])
    chiffa=IntegerField(label='Num Chiffa', validators=[])
    entrydate = DateField("Date d'entre", format='%d/%m/%Y')
    exitdate=DateField("Date de sortie", format='%d/%m/%Y',validators=[validators.optional()])
    submit=SubmitField(label='Enregistrer')
    