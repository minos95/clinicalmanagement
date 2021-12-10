import os
import datetime

from clinical import app,db
from flask import render_template ,redirect, url_for,request,flash,jsonify
from clinical.models import Patient ,Surgery,Checkup,Admin
from clinical.forms import RegisterForm,SurgeryForm,CheckupForm,LoginsForm,UpdateExite
from werkzeug.utils import secure_filename
from flask_login import login_user,logout_user,login_required
from sqlalchemy import or_,desc ,extract,and_ ,func



@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form=LoginsForm()
    error=""
    if form.validate_on_submit():
        attempted_user=Admin.query.filter(Admin.username==form.username.data).first()
        print(attempted_user)
        #print(attempted_user.id)



        if attempted_user and form.password.data=='admin' :
            print('login')
            login_user(attempted_user)
            return redirect(url_for('dashboard_page'))
        else:
            flash("le nom de l'utilisateur ou le mot de passe est incorect",category="danger")
            error="le nom de l'utilisateur ou le mot de passe est incorect"
    if form.errors!={}:
        for err_msg in form.errors.values():

            flash("il y\'as une erreur:{}".format(err_msg),category='danger')
    return render_template('index.html',form=form , nonavbar="",error=error)


@app.route('/dashboard')
@login_required
def dashboard_page():
    patients=Patient.query.order_by(desc(Patient.id)).limit(5).all()
    totalpatients=Patient.query.count()
    today=datetime.datetime.today()
    mounthPatients=Patient.query.filter(and_(extract('month', Patient.date_added) == today.month,extract('year', Patient.date_added) == today.year)).count()
    todayPatient=Patient.query.filter(and_(extract('day', Patient.date_added) == today.day,extract('month', Patient.date_added) == today.month,extract('year', Patient.date_added) == today.year)).count()
    hospitalized=Patient.query.filter(today<Patient.exitdate).count()
    print(hospitalized)
    surgeryData=db.session.query(Surgery.name,func.count(Surgery.name)).group_by(Surgery.name).all()
    labels=[str(item[0]) for item in surgeryData]
    values=[row[1] for row in surgeryData]
    return render_template('dashboard.html',patients=patients,totalpatients=totalpatients,
    mounthPatients=mounthPatients,todayPatient=todayPatient ,labels=labels,values=values,hospitalized=hospitalized)
@app.route('/patients',methods=['GET','POST'])
@login_required
def patients_page():
    if request.args.get("search"):
        patients=Patient.query.order_by(desc(Patient.id)).filter(or_(Patient.lastname == request.args.get("search"), Patient.identitynbr == request.args.get("search"))).paginate(per_page=20,page=int(request.args.get("page_num")),error_out=True)
    else:
        patients=Patient.query.order_by(desc(Patient.id)).paginate(per_page=20,page=int(request.args.get("page_num")),error_out=True)

    return render_template('patients.html',patients=patients)

@app.route('/patientShow',methods=['GET','POST'])
def patientShow():
    id=request.args.get("patient")
    form=UpdateExite()
    if form.validate_on_submit():
        print('submit')
        patient=Patient.query.filter(Patient.id==id).first()
        print(patient)
        patient.exitdate=form.exitDate.data
        db.session.commit()
        
    print(id)
    patient=Patient.query.filter_by(id=id).first()
    if request.args.get("action") and request.args.get("action")=="delete_surgery":
        id_surgery=request.args.get("surgery")
        surgery=Surgery.query.filter_by(id=id_surgery).first()
        db.session.delete(surgery)
        db.session.commit()
        return redirect(url_for('patientShow',patient=id))
    if request.args.get("action") and request.args.get("action")=="delete_checkup":
        id_checkup=request.args.get("checkup")
        checkup=Checkup.query.filter_by(id=id_checkup).first()
        db.session.delete(checkup)
        db.session.commit()
        return redirect(url_for('patientShow',patient=id))
    if request.args.get("action") and request.args.get("action")=="delete_patient":
        print('delete patient')
        db.session.delete(patient)
        db.session.commit()
        return redirect(url_for('patients_page',page_num=1))
    if request.args.get("action") and request.args.get("action")=="exit_patient":
        patient=Patient.query.filter_by(id=id).first()

        patient.exitdate=datetime.datetime.now()
        session.commit()
        return redirect(url_for('patientShow',patient=id))

    return render_template('patientShow.html',patient=patient,form=form)

@app.route('/registerPatient',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        
        patient_to_create=Patient(firstname=form.firstname.data,
                                  lastname=form.lastname.data,
                                  age=form.age.data,
                                  address=form.address.data,
                                  phone=form.phone.data,
                                  identitynbr=form.identity.data,
                                  chiffanbr=form.chiffa.data,
                                  entrydate=form.entrydate.data,
                                  exitdate=form.exitdate.data,
                                 )
        db.session.add(patient_to_create)
        db.session.commit()
        print('db executed')
        return redirect(url_for('patients_page',page_num=1))
    if form.errors!={}:
        for err_msg in form.errors.values():
            print(err_msg)
    return render_template('registerPatient.html', form=form)

@app.route('/registerSurgery',methods=['GET','POST'])
def register_surgery():
    form=SurgeryForm()
    id=request.args.get("patient")

    if form.validate_on_submit():
        surgery_to_create=Surgery(name=form.surgery_title.data,
                                doctor=form.doctor.data,
                                anesthesist=form.anesthesist.data,
                                date=form.date.data,
                                patient=id)

        db.session.add(surgery_to_create)
        db.session.commit()

        print('db executed')
        return redirect(url_for('patientShow',patient=id))
    if form.errors!={}:
        for  err_msg in form.errors.values():

            flash("il y\'as une erreur: {}".format(err_msg),category='danger')
    return render_template('registerSurgery.html', form=form)

@app.route('/registerCheckup',methods=['GET','POST'])
def register_checkup():
    form=CheckupForm()
    id=request.args.get("patient")
    if form.validate_on_submit():
        if form.file.data.filename is not None :
            filename = secure_filename(form.file.data.filename)
            form.file.data.save('clinical/static/uploads/' + filename)
            checkup_to_create=Checkup(name=form.checkup_title.data,
                                    path=filename,
                                    patient=id)
           
        else :
            checkup_to_create=Checkup(name=form.name.data,
                                    patient=id)
        db.session.add(checkup_to_create)
        db.session.commit()
        return redirect(url_for('patientShow',patient=id))
    return render_template('registerCheckup.html', form=form)
@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('index'))
@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    print('autocomplete')
    print(request.args.get('q'))
    search = request.args.get('q')
    query = db.session.query(Surgery.name).filter(Surgery.name.like('%' + 'prostate' + '%')).all()
    results = [mv[0] for mv in query]
    return jsonify(matching_results=results)