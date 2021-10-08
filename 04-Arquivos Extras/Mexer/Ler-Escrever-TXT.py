ref_arquivo = open("C:\\Users\\Alexandre\\Desktop\\a\\01.txt","r")

arq_1 = open("C:\\Users\\Alexandre\\Desktop\\a\\saida.txt","w")

contador = 1
for linha in ref_arquivo:
    
    if linha.find('AV=') > 0:
        valores = linha[linha.find('AV='):].split()
        # valores.append(valores)
        valores.remove('-----*-----')
        print(valores)
        
        escrever = "R"+str(contador)+"=" + str(valores[1])+'\n'
        print('Escrever: {}'.format(escrever))
        contador = contador + 1
        arq_1.write(escrever)
        
        escrever = "R"+str(contador)+"=" + str(valores[3])+'\n'
        print('Escrever: {}'.format(escrever))
        contador = contador + 1
        arq_1.write(escrever)
    elif linha.find('DV=') > 0:
        
        valores = linha[linha.find('DV='):].split()
        
        escrever = "R"+str(contador)+"=" + str(valores[1])+'\n'
        contador = contador + 1
        arq_1.write(escrever)
        
        escrever = "R"+str(contador)+"=" + str(valores[3])+'\n'
        contador = contador + 1
        arq_1.write(escrever)
    elif linha.find('LT=') > 0:

        valores = linha[linha.find('LT='):].split()
        
        escrever = "R"+str(contador)+"=" + str(valores[1])+'\n'
        contador = contador + 1
        arq_1.write(escrever)        


ref_arquivo.close()
arq_1.close() 


