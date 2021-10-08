from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from Functions.functions import *
from Paths.paths import PathEntrada

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    x='R10'
    print('Site Atualizou')
    dados = buscarTxtR()
    standard = buscarStandardR()
    correcoes = buscarCorrecao()
    if request.method == 'POST':
        print('metodo post')
        if 'botoes1' in request.form: #botao enviar R1
            salvarCorrecaoR1()
            File_exists=checartxt()
            if File_exists==True:
                x= 'R1'
            escrevertxtAll(x)
            return redirect(url_for('views.home'))
        elif 'botoes2' in request.form: #botao enviar R2
            salvarCorrecaoR2()
            x='R2'
            escrevertxtAll(x)
            return redirect(url_for('views.home'))
        elif 'botoes3' in request.form: #botao enviar R3
            salvarCorrecaoR3()
            x='R3'
            escrevertxtAll(x)
            return redirect(url_for('views.home'))
        elif 'botoes4' in request.form: #botao enviar R4
            salvarCorrecaoR4()
            x='R4'
            escrevertxtAll(x)
            return redirect(url_for('views.home'))
        elif 'botoesAll' in request.form: #botao enviar RAll
            salvarTodasCorrecoes()
            x='RAll'
            escrevertxtAll(x)
            return redirect(url_for('views.home'))
        elif 'botoesler' in request.form: #botao ler txt
            diretorio=PathEntrada
            dados=call3D(diretorio)
            return redirect(url_for('views.home'))
        else: 
            print('Else1: {}'.format(request.form))
    return render_template("home.html", user=current_user, medidas=dados, standard=standard, correcoes=correcoes)








    
