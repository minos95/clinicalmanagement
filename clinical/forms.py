from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,validators,PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import  Length, DataRequired 
from flask_wtf.file import FileField
class RegisterForm(FlaskForm):
    lastname=StringField(label='Nom', validators=[Length(min=2,max=30),DataRequired()],render_kw={'placeholder':'country'})
    firstname=StringField(label='Prenom', validators=[Length(min=2,max=30), DataRequired()])
    age=IntegerField(label='Age', validators=[ DataRequired()])
    address=StringField(label='Address')
    phone=StringField(label='Telephone')
    identity=IntegerField(label='Num Identite', validators=[ DataRequired()])
    chiffa=IntegerField(label='Num Chiffa', validators=[])
    entrydate = DateField("Date d'entre", format='%Y-%m-%d')
    exitdate=DateField("Date de sortie", format='%Y-%m-%d',validators=[validators.optional()])
    submit=SubmitField(label='Enregistrer')
    

class SurgeryForm(FlaskForm):
    name=StringField(label='Type dintervention', validators=[Length(min=2,max=30),DataRequired()])
    doctor=StringField(label='Operateur', validators=[Length(min=2,max=30), DataRequired()])
    anesthesist=StringField(label='Anesthesist', validators=[Length(min=2,max=30), DataRequired()])
    date = DateField("La date de l'intervention", format='%Y-%m-%d')
    submit=SubmitField(label='Enregistrer')
    

class CheckupForm(FlaskForm):
    name=StringField(label='Type de bilan', validators=[Length(min=2,max=30),DataRequired()])
    file = FileField(label='file')
    

    submit=SubmitField(label='Enregistrer')


class LoginsForm(FlaskForm):
    username=StringField(label='Utilisateur', validators=[Length(min=2,max=30),DataRequired()])
    password=PasswordField(label='Mot de passe', validators=[Length(min=2,max=30), DataRequired()])
    submit=SubmitField(label='Connexion')
    
class DoctorForm(FlaskForm):
    firstname=StringField(label='fisrtname', validators=[Length(min=2,max=30),DataRequired()])
    lastname=StringField(label='Lastname', validators=[Length(min=2,max=30),DataRequired()])
    #email=StringField(label='email', validators=[Email()])
    phone=StringField(label='phone')
    speciality=StringField(label='specialty', validators=[Length(min=2,max=30),DataRequired()])
    submit=SubmitField(label='Enregistrer')
    
class UpdateExite(FlaskForm):
    exitDate = DateField("La date de sortie", format='%Y-%m-%d')
    submit=SubmitField(label='Enregistrer')