# barn-culo-estudioso
Programas básicos de aprendizado :)

Quebrando Números usando Modúlos From/Import

from math import floor

num  = float (input('Digite um numero: '))
porção = floor(num)
print (' O numero {} tem a parte inteira {}'.format(num,porção))

'''Usando o modulo "Trunc" que faz o corte na parte inteira do numero'''

Import math
num  = float (input('Digite um numero: '))
print (' O numero {} tem a parte inteira {}'.format(num, math.trunc(num)))


Outra maneira simples ja interna 

num  = float (input('Digite um numero: '))
print (' O numero {} tem a parte inteira {}'.format(num, int(num)))
