import sqlite3
from Paths.paths import BancoSQL
import os.path



conn = sqlite3.connect('BancoSQL.db', check_same_thread=False)
c = conn.cursor()

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------CREATE-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#Essa funcao cria a tabela VALORES, criando também 4 variaveis R1, R2, R3 e R4
def createTableMedidas():
    c.execute(""" CREATE TABLE IF NOT EXISTS TabelaValores(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    R1 NUMBER,
    R2 NUMBER,
    R3 NUMBER,
    R4 NUMBER
    )""")
#Essa funcao cria a tabela Padrao, criando também 4 variaveis R1, R2, R3 e R4 dentro dela.
#A tabela padrao serve para armazenar o valor padrao da peça.
#Esse valor padrao sera buscado para efetuar o calculo de correção.
def createTablePadrao():
    c.execute(""" CREATE TABLE IF NOT EXISTS TabelaPadrao(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    R1 NUMBER,
    R2 NUMBER,
    R3 NUMBER,
    R4 NUMBER
    )""")
#Cria a tabela correcao
def createTableCorrecao():
    c.execute(""" CREATE TABLE IF NOT EXISTS TabelaCorrecao(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    R1 NUMBER,
    R2 NUMBER,
    R3 NUMBER,
    R4 NUMBER
    )""")
#Cria todas as tabelas
def createAllTables():
    createTableMedidas()
    createTablePadrao()
    createTableCorrecao()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------DELETE-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def deleteAllTables():
    c.execute("""DROP TABLE IF EXISTS TabelaValores""")
    c.execute("""DROP TABLE IF EXISTS TabelaPadrao""")
    c.execute("""DROP TABLE IF EXISTS TabelaCorrecao""")
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------INSERT-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
    #nomeTabela: o usuario precisa passar o nome da tabela
    #dados: LISTA com os dados
    #para cada dado em dados, faça:
    #dadosInternos atribui, ela mesma + cada dado em forma de string + 1 virgula +1 espaço no final
    #note que no ultimo dado ele vai receber uma virgula e o espaço também, causando erro de sintaxe
    #esse erro é arrumado fora do for
def inserir_R1_R2_R3_R4(nomeTabela, listaComOsValores): 
    dadosInternos=""
    for dado in listaComOsValores:
        dadosInternos=dadosInternos+str(dado)+", "
    #aqui deleta a virgula e o espaço no final
    #aqui da um insert na tabela passada como parametro pelo usuario, do conjunto de valore R1,R2,R3 e R4
    #commit = confirma
    dadosInternos=dadosInternos[:-2]
    c.execute("""INSERT INTO """+nomeTabela+"""(R1, R2, R3, R4) VALUES("""+dadosInternos+""")""")
    conn.commit()
    return True


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------UPDATE-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def updateR(nomeTabela, variavel_R_com_numero, valor, id):
    c.execute("""UPDATE """+nomeTabela+""" SET """+variavel_R_com_numero+""" ='"""+valor+"""' WHERE id = '"""+id+"""';""")
    conn.commit()
def updateR1_R2_R3_R4(nomeTabela, listaComOsValores):
    dadosInternos=""
    for dado in listaComOsValores:
        dadosInternos=dadosInternos+str(dado)+", "
    dadosInternos=dadosInternos[:-2] #deleta o ponto e virgula no final
    c.execute("""UPDATE """+nomeTabela+""" SET (R1, R2, R3, R4) VALUES("""+dadosInternos+""")""")
    conn.commit()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------RESET-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def resetTables():
    deleteAllTables()
    createAllTables()
    zerar = (0, 0, 0, 0)
    inserir_R1_R2_R3_R4('TabelaCorrecao', zerar)
    inserir_R1_R2_R3_R4('TabelaValores', zerar)
    inserir_R1_R2_R3_R4('TabelaPadrao', zerar)
    print('tabelas resetadas')

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------------------SELECT-------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def selectR(nomeTabela, variavel_R_com_numero, id):
    variavel=''
    c.execute("""SELECT """+variavel_R_com_numero+""" FROM '"""+nomeTabela+"""' WHERE id = '"""+id+"""';""")
    variavel=c.fetchall()
    for x in variavel:
        x=x[0]
    return x

def checkDBExists():
    a=()
    a= c.execute(""" SELECT count(*) FROM sqlite_master WHERE type='table' AND name='TabelaValores' COLLATE NOCASE;""")
    a=c.fetchone()
    for b in a:
        if b == 1:
            print('Tabelas ja existem, Tudo Certo!')
        elif b == 0:
            resetTables()
            
        else:
            print('Problema...Ver ManageDB')

checkDBExists()
