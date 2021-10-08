from Manage.manageDB import *
from flask import flash
from Paths.paths import PathSaida
import sqlite3
import os

conn = sqlite3.connect('BancoSQL.db', check_same_thread=False)
c = conn.cursor()

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------3D-----------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#Buscar info da 3D chamando a funcao "Processamentodearquivo" abaixo.
def call3D(diretorioDeArquivo):
    medidas_recebe= Processamentodearquivo(diretorioDeArquivo)
    return medidas_recebe
#Esta funcao tem o intuito de abrir o arquivo txt no totem da tridimencional
#buscar os valores R1,R2,R3 e R4
#E jogar nas variaveis [Heller_R1, Heller_R2, Heller_R3, Heller_R4]
def Processamentodearquivo(diretorioArquivo):
    arquivo1 = open(diretorioArquivo , 'r')
    lista = lertxtR1R2R3R4(arquivo1)
    Heller_R1 = lista[0]
    Heller_R2 = lista[1]
    Heller_R3 = lista[2]
    Heller_R4 = lista[3]
    arquivo1.close()
    return [Heller_R1, Heller_R2, Heller_R3, Heller_R4]
#-----------------------------------------------------------------------------------
def checartxt():
        if(os.path.exists(PathSaida)):
            print('O Arquivo Existe')
            return True
        else:
            print('O Arquivo Nao Existe')
            return False
def criartxt():
    return
def lertxtR1R2R3R4(arquivo1):
    contador = 1
    for linha in arquivo1:
        if linha.find('AV=') > 0:
            valores = linha[linha.find('AV='):].split()
            if contador == 1:
                Heller_R1 = valores[1]
                updateR('TabelaValores','R1', Heller_R1, '1')
            elif contador == 2:
                Heller_R2 = valores[1]
                updateR('TabelaValores','R2', Heller_R2, '1')
            elif contador == 3:
                Heller_R3 = valores[1]  
                updateR('TabelaValores','R3', Heller_R3, '1')
            elif contador == 4:
                Heller_R4 = valores[1]
                updateR('TabelaValores','R4', Heller_R4, '1')
            contador = contador + 1
    flash('TXT file sucessfully loaded')
    return [Heller_R1, Heller_R2, Heller_R3, Heller_R4]

def escrevertxtAll(R):
    try:
        file = open(PathSaida, 'w')
        string = R
        print(string)
        if string == 'R1':
            string = selectR('TabelaCorrecao', str(string), '1')
            escrever = 'R1=' + str(string) + '\n'
            file.write(escrever)
            lista = buscarCorrecao()
            print('lista[6]: {}'.format(lista[5]))
            escrever = 'R2=' + str(lista[5]) + '\n'
            file.write(escrever)
            print('lista[7]: {}'.format(lista[6]))
            escrever = 'R3=' + str(lista[6]) + '\n'
            file.write(escrever)
            print('lista[8]: {}'.format(lista[7]))
            escrever = 'R4=' + str(lista[7]) + '\n'
            file.write(escrever)
        elif string == 'R2':
            lista = buscarCorrecao()
            escrever = 'R1=' + str(lista[4]) + '\n'
            file.write(escrever)
            string = selectR('TabelaCorrecao', str(string), '1')
            escrever = 'R2=' + str(string) + '\n'
            file.write(escrever)
            escrever = 'R3=' + str(lista[6]) + '\n'
            file.write(escrever)
            escrever = 'R4=' + str(lista[7]) + '\n'
            file.write(escrever)
        elif string == 'R3':
            lista = buscarCorrecao()
            escrever = 'R1=' + str(lista[4]) + '\n'
            file.write(escrever)
            escrever = 'R2=' + str(lista[5]) + '\n'
            file.write(escrever)
            string = selectR('TabelaCorrecao', str(string), '1')
            escrever = 'R3=' + str(string) + '\n'
            file.write(escrever)
            escrever = 'R4=' + str(lista[7]) + '\n'
            file.write(escrever)
        elif string == 'R4':
            lista = buscarCorrecao()
            escrever = 'R1=' + str(lista[4]) + '\n'
            file.write(escrever)
            escrever = 'R2=' + str(lista[5]) + '\n'
            file.write(escrever)
            escrever = 'R3=' + str(lista[6]) + '\n'
            file.write(escrever)
            string = selectR('TabelaCorrecao', str(string), '1')
            escrever = 'R4=' + str(string) + '\n'
            file.write(escrever)
        elif string == 'RAll':
            for i in range(1,5):
                string = 'R' + str(i)
                string = selectR('TabelaCorrecao', str(string), '1')
                escrever = 'R'+str(i)+'=' + str(string) + '\n'
                file.write(escrever)
        else:
            print('Nao Consegui escrever o documento')
        file.close()
        return True
    except:
        flash('Error Writing TXT')
        return False
    
def buscarCorrecao():
    standard_R1=selectR('TabelaPadrao','R1', '1')
    medida_R1=selectR('TabelaValores','R1', '1')
    standard_R2=selectR('TabelaPadrao','R2', '1')
    medida_R2=selectR('TabelaValores','R2', '1')
    standard_R3=selectR('TabelaPadrao','R3', '1')
    medida_R3=selectR('TabelaValores','R3', '1')
    standard_R4=selectR('TabelaPadrao','R4', '1')
    medida_R4=selectR('TabelaValores','R4', '1')
    oldCorrectionR1=selectR('TabelaCorrecao', 'R1', '1')
    oldCorrectionR2=selectR('TabelaCorrecao', 'R2', '1')
    oldCorrectionR3=selectR('TabelaCorrecao', 'R3', '1')
    oldCorrectionR4=selectR('TabelaCorrecao', 'R4', '1')
    correcao_R1 = standard_R1 - medida_R1
    correcao_R2 = standard_R2 - medida_R2
    correcao_R3 = standard_R3 - medida_R3
    correcao_R4 = standard_R4 - medida_R4
    correcoes = (correcao_R1, correcao_R2, correcao_R3, correcao_R4, oldCorrectionR1, oldCorrectionR2, oldCorrectionR3, oldCorrectionR4)
    return (correcoes)

def salvarCorrecaoR1():
    standard_R1=selectR('TabelaPadrao','R1', '1')
    medida_R1=selectR('TabelaValores','R1', '1')
    correcao_R1 = standard_R1 - medida_R1
    updateR('TabelaCorrecao', 'R1', str(correcao_R1), '1')
    return
def salvarCorrecaoR2():
    standard_R2=selectR('TabelaPadrao','R2', '1')
    medida_R2=selectR('TabelaValores','R2', '1')
    correcao_R2 = standard_R2 - medida_R2
    updateR('TabelaCorrecao', 'R2', str(correcao_R2), '1')
    return
def salvarCorrecaoR3():
    standard_R3=selectR('TabelaPadrao','R3', '1')
    medida_R3=selectR('TabelaValores','R3', '1')
    correcao_R3 = standard_R3 - medida_R3
    updateR('TabelaCorrecao', 'R3', str(correcao_R3), '1')
    return
def salvarCorrecaoR4():
    standard_R4=selectR('TabelaPadrao','R4', '1')
    medida_R4=selectR('TabelaValores','R4', '1')
    correcao_R4 = standard_R4 - medida_R4
    updateR('TabelaCorrecao', 'R4', str(correcao_R4), '1')
    return
def salvarTodasCorrecoes():
    salvarCorrecaoR1()
    salvarCorrecaoR2()
    salvarCorrecaoR3()
    salvarCorrecaoR4()
    return

def buscarTxtR():
    Valor_R1= selectR('TabelaValores', 'R1', '1')
    Valor_R2= selectR('TabelaValores', 'R2', '1')
    Valor_R3= selectR('TabelaValores', 'R3', '1')
    Valor_R4= selectR('TabelaValores', 'R4', '1')
    dados=[Valor_R1,Valor_R2,Valor_R3,Valor_R4]
    return dados

def buscarStandardR():
    Standard_R1 = selectR('TabelaPadrao', 'R1', '1')
    Standard_R2 = selectR('TabelaPadrao', 'R2', '1')
    Standard_R3 = selectR('TabelaPadrao', 'R3', '1')
    Standard_R4 = selectR('TabelaPadrao', 'R4', '1')
    standard = [Standard_R1, Standard_R2, Standard_R3, Standard_R4]
    return standard
