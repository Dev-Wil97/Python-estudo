# barn-culo-estudioso
Programas básicos de aprendizado :)

# Fazendo um profeesor sortear algum aluno ^^

from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido)) 
