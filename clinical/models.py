
import datetime
from clinical import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False)
    password=db.Column(db.String(length=30),nullable=False)
    
   
   
    #def check_password(self,attempted_password):
     #   print(self.username)
      #  if  'admin' ==self.password:
       #     return True
        #else:
         #   return False
           

class Patient(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    firstname=db.Column(db.String(length=30),nullable=False)
    lastname=db.Column(db.String(length=30),nullable=False)
    address=db.Column(db.String(length=30),nullable=False)
    age=db.Column(db.Integer(),nullable=False)
    phone=db.Column(db.String(length=15),nullable=False)
    identitynbr=db.Column(db.Integer(),nullable=False)
    chiffanbr=db.Column(db.Integer(),nullable=False)
    date_added=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    entrydate=db.Column(db.Date())
    exitdate=db.Column(db.Date())
    surgeries=db.relationship('Surgery',backref='patient_surgery',cascade="all,delete",lazy=True)
    checkups=db.relationship('Checkup',backref='patient_checkup',cascade="all,delete",lazy=True)
    #def __repr__(self):
    #   return f Patient {self.name}
class Surgery(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    doctor=db.Column(db.String(length=30),nullable=False)
    anesthesist=db.Column(db.String(length=30),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    patient=db.Column(db.Integer(),db.ForeignKey('patient.id'))
    date_added=db.Column(db.DateTime, default=datetime.datetime.utcnow)
   # def __repr__(self):
   #     return f'Surgery {self.name}'

class Checkup(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    path=db.Column(db.String(length=30),nullable=False)
    patient=db.Column(db.Integer(),db.ForeignKey('patient.id'))
    date_added=db.Column(db.DateTime, default=datetime.datetime.utcnow)