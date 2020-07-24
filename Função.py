#a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor
# qualquer, baseada em um loop (for).
#O objetivo das funcoes é agilizar o processo

import numpy as np
def média (vetor): #def usado para criar uma função. média é no nome da função. (vetor) é argumento
    soma = 0 # estrutura que capita os valores um por um.
    it = 0 #iterador
    for i in vetor: #i é o elemento que vamos acessar! dentro(in) do vetor.

        soma += i # somador = somador + i
        it+=1 # it = it+1
    mean = soma/it
    return mean

def variancia (vetor):
    soma = 0
    it = 0
    sdq = 0
    for i in vetor:

        soma += i  # soma = soma + i
        it += 1  # it = it+1
        sdq += i**2 #sdq = sdq + i**2

    var = (sdq - ((soma**2/it)))/(it-1)
    return var
##quando rodamos essa função não acontesse nada pois apenas criamos devemos agora usa-la nos dados.


