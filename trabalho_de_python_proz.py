print ("atividade de python: Tabuada")
print ("aluno: Luis Fernando Araujo Ferraz")
numero = float(input('digite o número inicial da tabuada: '))

num2 = int(input('digite áte que número essa tabuada vai: '))

for fator in range(1,num2+1):
    print('Trabalho')
    print(f'{numero} x {fator} = {numero*fator}')
