from flask_wtf import FlaskForm
from wtforms import DateField,StringField, SubmitField,IntegerField,PasswordField
from wtforms.validators import  Length, DataRequired
class LoginsForm(FlaskForm):
    username=StringField(label='Utilisateur', validators=[Length(min=2,max=30),DataRequired()])
    password=PasswordField(label='Mot de passe', validators=[Length(min=2,max=30), DataRequired()])
    submit=SubmitField(label='Connexion')
    