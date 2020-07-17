print('DATA: 04/07/2020')
print('DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS')
print('PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO')
print('DISCENTE: EWERTON LELYS RESENDE')
'''
# print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(
    '###################################################################################################################')
print('REO 01 - LISTA DE EXERCÍCIOS')

print('EXERCÍCIO 01:')
print('a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
import numpy as np

a = np.array([43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15])
print(a)
print(' ')

print('b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
dim_01 = len(a)
print('Dimensão (dim_01): ' + str(dim_01))
média = np.mean(a)
print('Média: ' + str(média))
maximo = np.max(a)
print('Máximo: ' + str(maximo))
minimo = np.min(a)
print('Mínimo: ' + str(minimo))
variancia = np.var(a)
print('Variância: ' + str(variancia))
print(' ')

print('c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor da média deste.')
média_v = np.mean(a)
print(média_v)
b = np.array((a-média_v)**2)
print('Vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento = ' + str(b))
media_b = np.mean(b)
print('Média deste vetor = ' + str(media_b) + '.Vale resaltar que esta, nada mais é que a variância do vetor a.')
print(' ')

print('d) Obtenha um novo vetor que contenha todos os valores superiores a 30.')
d = a > 30
dv = a[d]
print('Vetor com todos os valores superiores a 30 = ', dv)
print(' ')

print('e) Identifique quais as posições do vetor original possuem valores superiores a 30')
e = np.where(a > 30) #np.where nos possibilita encontrar o valor dentro da matriz
print('Posições do vetor original com valores superiores a 30 = ', e[0])
# [0,primeiro elemento é o que tem valor menos que 30
print(' ')

print('f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
f = a[[0, 4, -1]]
print('Vetor com os valores da primeira, quinta e última posição = ', f)
print(' ')

print('g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações')
# iterador
# a estrutura de repetição inicia com FOR, seguido de uma variável (valor), in (dentro) da lista;
# a delimitação de deve a indentação
# sendo que a cada iteração o (valor) recebe cada elemento da lista.
numero_de_elementos = len(a)
print(numero_de_elementos)
lista = list(range(0, len(a), 1))
print('Lista de posições = ', str(lista))
it = 0
for valor in range(0, len(a), 1):  # indica as posicoes dos valores de um vetor que se deseja trabalhar
    it = it + 1
    print('Posição = ' + str(valor))
    print('Valor = ' + str(
        a[int(valor)]))  # int é uma necessidade de tranformar o valor em inteiro, para podermos acessar posiçoes .
    print('-'*51)
print(" Podemos também utlizar a função ENUMERATE")
it = 0
for pos, alt in enumerate(a):  # pega o elemento nossa lista (altura) e a posição deste!
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(pos) + ' há o elemento: ' + str(alt))
    print('-'*51)
print(' ')

print('h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
n = np.shape(a)
print(n)
vetor = np.zeros(n)
print(vetor)
tipo = type(a)
print(tipo)
for sq in np.arange(0, 9, 1):
    print('Valores_sq = ' + str(a[int(sq)]))
    vetor[int(sq)] = (a[int(sq)])**2

print('Valores ao Quadrados = ' + str(vetor))
soma = np.sum(vetor)
print('Soma de quadrados = ' + str(soma))
print(' ')

print('i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
 #parecido com FOR, tem ter que indentação,
# tem uma condição, que quando atingida para contador != 15
tv = 0
while a[tv] != 100:
    print('Posição = ' +str(tv+1))
    print('Valor = ' +str(a[tv]))
    print('-' * 50)
    tv = tv+1
    if tv == (len(a)):
        break
print(' ')

print('j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
seq = np.arange(1, 10, 1)
seq = np.array(seq)
print('Sequência de valores ' + str(seq))
print(' ')

print("h) Concatene o vetor da letra a com o vetor da letra j.")
h = np.concatenate((a, seq))
print('Concatenação de vetore ' + str(h))
len(h)
print("Tamanho = " + str(h))
print(' ')
print('-='*100)
print(' ')
print('EXERCÍCIO 02:')
print('a) Declare a matriz abaixo com a biblioteca numpy.')
# 1 3 22
# 2 8 18
# 3 4 22
# 4 1 23
# 5 2 52
# 6 2 18
# 7 2 25
matriz = np.array([[1,3,22],
          [2,8,18],
          [3,4,22],
          [4,1,23],
          [5,2,52],
          [6,2,18],
          [7,2,25]])
print('Matriz usando NumPy')
print(matriz)
print(' ')

print('b) Obtenha o número de linhas e de colunas desta matriz')
nl,nc = np.shape(matriz)
print('Linhas = ' + str(nl))
print('Colunas = ' + str(nc))
print(' ')

print('c) Obtenha as médias das colunas 2 e 3.')
media_c2 = np.mean(matriz[:,1])
print('Média da coluna 2 = ' + str(media_c2))
media_c3 = np.mean(matriz[:,2])
print('Média da coluna 3 = ' + str(media_c3))
print(' ')

print('d) Obtenha as médias das linhas considerando somente as colunas 2 e 3')
sub_matriz = matriz[0:,1:] # quer dizer que 0:. vai da linha 1 ate o final das linhas
#,1:] vai da coluna 2 até o final das colunas
print(sub_matriz)
#test_sm = matriz[5:,0:] #5: quer dizer que vai de linha 6 até o final
# 0: coluna 1 até o final.
#print(test_sm)
for i in np.arange(0, nl, 1):
    media_linhas = np.mean(sub_matriz[[i], [0, 1]])
    print('Média da linha ' + str(i+1) + ' = ' + str(media_linhas))

#media_linhas = np.mean(sub_matriz[0,:]) #eu fiz da linha 1 mas como fazer de todas as linhas???
#print(media_linhas)
print(' ')

print('e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. '
      'Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print(matriz)
print(' ')
notas = matriz[0:,1:2]
print(notas)
p_notas_menores_5 = np.where(notas<5)
print('Posições das notas menores que 5 = ' ,p_notas_menores_5[0])
gen = matriz [0:,0]
print('Genótipos = ' + str(gen))
gen_r = gen[[0, 2, 3, 4, 5, 6]]
print('Genótipos resistentes = ' ,gen_r)
print(' ')

print('f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. '
      'Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
peso = matriz[0:,2:]
print(peso)
peso_m_22 = np.where(peso>=22) # testa as condiçoes 
print('Posições das notas de peso de 100 grãos maiores ou igual a 22 = ' ,peso_m_22[0])
gen = matriz [0:,0]
print('Genótipos = ' + str(gen))
gen_p = gen[[0,2,3,4,6]]
print('Genótipos com peso de 100 grãos maiores ou igual a 22 = ' ,gen_p)
print(' ')

print('g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. '
      'Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100 grãos igual ou superior a 22.')

print('Posições das notas de peso de 100 grãos maiores ou igual a 22 = {}. Posições das notas menores que 5 = {}'.format(peso_m_22[0], p_notas_menores_5[0]))
#g = gen[peso_m_22 & p_notas_menores_5]
#print(g)

print(' ')
print('h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu'
      'respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido.'
      'Apresente a seguinte mensagem a cada iteração (Na linha X e na coluna Y ocorre o valor: Z'
      'Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
matriz_h = [] #Matriz onde será armazenado nossos dados.
it = 0 #iterador é um munero inteiro que recebe 0 como primeiro valor. mas está fora do FOR

# Função np.range(uma sequencia), gerar uma nova lista! informamos o primeiro valor no caso 0;
# informamos as dimenções de linhas e colunas, 7 e 3,respectivamente. o qual não entra na sequencia.
# sendo 1 o passo a ser executado( soma um a cada elemento)
for i in np.arange(0, 7, 1):
    for j in np.arange(0, 3, 1):
        it = it + 1
        print('Iteração = ' + str(it))
        print('Na linha ' + str(i+1) +
              ' e na coluna ' + str(j+1)+
              ' ocorre o Valor = ' + str(matriz[int(i), int(j)]))
        matriz_h = (matriz[:,2]>=25)
        matriz_25 = (matriz[matriz_h])
print(matriz_h)
print(matriz_25)
gen_prod = matriz_25[:,0] # ANTES DA VIRGULA É LINHA, APÓS É COLUNA! Quando eu coloco nada antes do dois pontos indica que vamos pegar todas as linhas
# O 0 após a virgula indica a posição da coluna que vamos pegar, no caso, posição 1.
# O : INDICA SEQUENCIA!!!
# ANTES DA , VAZIO INDICA PEGAR TODAS AS LINHAS!
print(' Os genótipos com prod. maior ou igual a 25 são os ' + str(gen_prod))
print(' ')
print('-='*100)
print(' ')

print('EXERCÍCIO 03:')
print('a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um loop (for).')
from função_a import summary
amostra = summary(a, 4, 5)
print('-'*50)
print('Resultado:')
print('  Sample     Mean     Var')
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print(str(amostra))
print('b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 '
      'e variância 2500. Pesquise na documentação do numpy por funções de simulação.')
import math
a_10 = np.random.normal(100, math.sqrt(2500), 10)
a_100 = np.random.normal(100, math.sqrt(2500), 100)
a_1000 = np.random.normal(100, math.sqrt(2500), 1000)
print('array_10 = np.random.normal(100, math.sqrt(2500), 10)')
print('array_100 = np.random.normal(100, math.sqrt(2500), 100)')
print('array_1000 = np.random.normal(100, math.sqrt(2500), 1000)')
#help(np.random.normal)
#print(a_10)
#print(a_100)
#print(a_1000)
print(' ')
print('c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.')

print('d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.')
import matplotlib.pyplot as plt
h10 = plt.hist(a_10)
h100 = plt.hist(a_100)
h1000 = plt.hist(a_1000)
h10000 = plt.hist(np.random.normal(100, math.sqrt(2500), 10000))

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.hist(a_10, color="tab:red")
ax0.set_title('n = 10')
ax1.hist(a_100, color="tab:orange")
ax1.set_title('n = 100')
ax2.hist(a_1000, color="tab:green")
ax2.set_title('n = 1000')
ax3.hist(np.random.normal(100, math.sqrt(2500), 10000), color="tab:blue")
ax3.set_title('n = 10000')
fig.tight_layout()
plt.show()
print(' ')
print('-='*100)
print(' ')
'''
print('EXERCÍCIO 04:')
print("a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a"
    "quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, "
    "apresente os dados e obtenha as informações de dimensão desta matriz.")

import numpy as np
from matplotlib import pyplot as plt
dados = np.loadtxt('dados.txt')
nl, nc = dados.shape
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print(dados)
print('Número de linhas = ' + str(nl))
print('Número de colunas = ' + str(nc))
print(' ')

print('b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
print('Usando help(), podemos acessar as informações de uma função!')
print('-'*51)
print('A função **np.unique**, serve para acharmos elementos específos de um vetor ou uma matrix')
#help(np.unique)
print('-'*51)
print('A função **np.where**, retorna elementos, de x ou y, dependendo da condição.')
#help(np.where)
print('-'*51)
print(' ')
print('c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas')
genotipos = np.unique(dados[0:30,0:1], axis=0) # quer dizer que vamos pegar os valores da linha 1 até a 31 e coluna 1 até a dois.
print('Genótipos = ' + str(genotipos))
rep = (np.unique(dados[0:30,1:2]))
print('Repetições = ' + str(len(rep)))
print(' ')

print('d) Apresente uma matriz contendo somente as colunas 1, 2 e 4')
sub_m = dados[:,[0,1,3]] #Após a vírgula são as colunas específicas que vamos pegar.
print('Matriz contendo as colunas 1, 2 e 4.')
print(sub_m)
print(' ')
print('e) Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.')
nlg = len(genotipos)
print(nlg)
minimos = np.zeros((nlg,1)) #Primeiro valor é numero de linhas da matriz (10 Genotipos) e o segundo o numero de colunas.
maximos = np.zeros((nlg,1))
medias = np.zeros((nlg,1))
variancia = np.zeros((nlg,1))

it = 0
for i in np.arange(0,nl,3):
    minimos[it,0] = np.min(sub_m[i:i + 3, 2], axis=0)
    maximos[it,0] = np.max(sub_m[i:i + 3, 2], axis=0)
    medias[it, 0] = np.mean(sub_m[i:i + 3, 2], axis=0)
    variancia[it, 0] = np.var(sub_m[i:i + 3, 2], axis=0)
    it = it + 1
#print(genotipos)
#print(minimos)
#print(maximos)
#print(medias)
#print(variancia)
m_c = np.concatenate((genotipos, minimos, maximos, medias, variancia), axis=1) # axis = eixo( ao colocarmos o axis =1 colocamos as colunas uma ao lado da outra.
print('Genótipos     Min     Max      Média  Variância')
print(m_c)
#help(np.savetxt)
np.savetxt('matriz_ex4.txt', m_c, fmt='%10.2f',delimiter=' ') #fmt format, significa que terá duas casas decimais.
print(' ')
print(type(m_c))
print('f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
gen_500 = m_c[:,3]>=500 #gera um vetor de verdadeiro ou falso, para os genótippos que possuem média superior a 500(verdadeiro)
print(gen_500)
f = m_c[gen_500]
print(f)
print('Genótipos com média igual ou superior a 500 = ' + str(f[:,0]))
print(' ')


print('g) Apresente os seguintes graficos:')
print('Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura')
from matplotlib import pyplot as plt
media1 = np.zeros((nlg,1))
media2 = np.zeros((nlg,1))
media3 = np.zeros((nlg,1))
media4 = np.zeros((nlg,1))
media5 = np.zeros((nlg,1))
it = 0
for i in np.arange(0,30,3): #numpy.arange([start, ]stop, [step, ]dtype=None)
    media1[it,0] = np.mean(dados[i:i + 3, 2], axis=0) # 2 significa que é a terceira coluna!
    media2[it,0] = np.mean(dados[i:i + 3, 3], axis=0)
    media3[it,0] = np.mean(dados[i:i + 3, 4], axis=0)
    media4[it,0] = np.mean(dados[i:i + 3, 5], axis=0)
    media5[it,0] = np.mean(dados[i:i + 3, 6], axis=0)
    it = it + 1
#print(media1)

v_c = np.concatenate((genotipos,media1,media2,media3,media4,media5),axis=1)
print(v_c)
plt.style.use('ggplot')
plt.figure('Grafíco das variáveis') #Create a new figure.
font = {'family': 'serif',
        'color':  'gray',
        'weight': 'normal',
        'size': 12,
        }
font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

plt.subplot(2,3,1) #Add a subplot to the current figure. #detremina a posição dos graficos ao mostra!
plt.bar(v_c[:,0],v_c[:,1]) #Make a bar plot.
plt.title('Variável 1 ', fontdict=font1)
plt.xticks(v_c[:,0])
plt.xlabel('Genótipos', fontdict=font)
plt.ylabel('Média', fontdict=font)

plt.subplot(2,3,2) #Add a subplot to the current figure. #detremina a posição dos graficos ao mostra!
plt.bar(v_c[:,0],v_c[:,2]) #Make a bar plot.
plt.title('Variável 2 ', fontdict=font1)
plt.xticks(v_c[:,0])
plt.xlabel('Genótipos', fontdict=font)
plt.ylabel('Média', fontdict=font)

plt.subplot(2,3,3) #Add a subplot to the current figure. #detremina a posição dos graficos ao mostra!
plt.bar(v_c[:,0],v_c[:,3]) #Make a bar plot.
plt.title('Variável 3 ', fontdict=font1)
plt.xticks(v_c[:,0])
plt.xlabel('Genótipos', fontdict=font)
plt.ylabel('Média', fontdict=font)

plt.subplot(2,3,4) #Add a subplot to the current figure. #detremina a posição dos graficos ao mostra!
plt.bar(v_c[:,0],v_c[:,4]) #Make a bar plot.
plt.text(5, 430, r'Variável 4 ', fontdict=font1)
plt.xticks(v_c[:,0])
plt.xlabel('Genótipos', fontdict=font)
plt.ylabel('Média', fontdict=font)

plt.subplot(2,3,5) #Add a subplot to the current figure. #detremina a posição dos graficos ao mostra!
plt.bar(v_c[:,0],v_c[:,5]) #Make a bar plot.
plt.text(5, 630, r'Variável 5 ', fontdict=font1)
plt.xticks(v_c[:,0])
plt.xlabel('Genótipos', fontdict=font)
plt.ylabel('Média', fontdict=font)
plt.show()
print(' ')

print('Dispesão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.')
plt.style.use('ggplot')
fig = plt.figure('Scatter plot 2D') #A scatter plot of y vs. x with varying marker size and/or color.
plt.subplot(2,2,1)
c = ['yellow','red','green','black','pink','black','orange','cyan','slategray','darkviolet']
for i in np.arange(0,10,1):
    plt.scatter(v_c[i,1], v_c[i,2], s=50,alpha=0.8,label = v_c[i,0],c = c[i])

plt.xlabel('Var 1', fontdict=font1)
plt.ylabel('Var 2', fontdict=font1)
plt.subplot(2,2,2)
for i in np.arange(0,10,1):
    plt.scatter(v_c[i,1], v_c[i,3], s=50, alpha=0.8, label = v_c[i,0], c=c[i])

plt.xlabel('Var 1', fontdict=font1)
plt.ylabel('Var 3', fontdict=font1)
plt.subplot(2,2,3)
for i in np.arange(0,10,1):
    plt.scatter(v_c[i,1], v_c[i,3], s=50, alpha=0.8, label = v_c[i,0], c=c[i])

plt.xlabel('Var 2', fontdict=font1)
plt.ylabel('Var 4', fontdict=font1)
plt.subplot(2,2,2)
for i in np.arange(0,10,1):
    plt.scatter(v_c[i,1], v_c[i,3], s=50, alpha=0.8, label = v_c[i,0], c=c[i])
plt.legend(bbox_to_anchor=(2.08, 0.7), title='Genotypes', borderaxespad=0., ncol=5)

plt.show()