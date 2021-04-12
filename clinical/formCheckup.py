from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import  Length, DataRequired
from flask_wtf.file import FileField
class CheckupForm(FlaskForm):
    name=StringField(label='Type de bilan', validators=[Length(min=2,max=30),DataRequired()])
    file = FileField(label='file')
    #path=StringField(label='prenom', validators=[Length(min=2,max=30), DataRequired()])
    

    submit=SubmitField(label='Enregistrer')
    