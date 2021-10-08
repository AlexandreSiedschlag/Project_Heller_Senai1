from flask import Blueprint, render_template, request, flash, redirect, url_for
from Functions.functions import *
from Website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, login_required, logout_user, current_user



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() #ta buscando o user do email mandado
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/padrao', methods=['POST', 'GET'])
@login_required
def padrao():
    if request.method == 'POST':
        try:
            print('POST')
            standard=''
            Standard_R1 = request.form.get('r1')
            Standard_R2 = request.form.get('r2')
            Standard_R3 = request.form.get('r3')
            Standard_R4 = request.form.get('r4')
            standard = [Standard_R1, Standard_R2, Standard_R3, Standard_R4]
            print(standard)
            contador =0
            for item in standard:
                contador = contador +1
                print(item)
                print(type(item))
                item = float(item)
                print(type(item))
                if type(item) == float or type(item) == int:
                    updateR('TabelaPadrao', 'R1', Standard_R1, '1')
                    updateR('TabelaPadrao', 'R2', Standard_R2, '1')
                    updateR('TabelaPadrao', 'R3', Standard_R3, '1')
                    updateR('TabelaPadrao', 'R4', Standard_R4, '1')
                    if contador >=4:
                        flash('New Values Added Into DataBase')                        
                else:
                    flash('Try typing only numbers, you can use dots')
        except:
            return redirect(url_for('auth.padrao')), flash('Try typing only numbers, you can use dots')
    else:
        try: 
            print('GET')
            Standard_R1= selectR('TabelaPadrao', 'R1', '1')
            Standard_R2= selectR('TabelaPadrao', 'R2', '1')
            Standard_R3= selectR('TabelaPadrao', 'R3', '1')
            Standard_R4= selectR('TabelaPadrao', 'R4', '1')
            standard=[Standard_R1, Standard_R2, Standard_R3, Standard_R4]
        except:
            flash('')

    return render_template('padrao.html', user=current_user, standard=standard)



    
