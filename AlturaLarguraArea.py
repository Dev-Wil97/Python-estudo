# barn-culo-estudioso
Calculando a Altura , Largura e Área , Para saber a quantidade de tinta que você irá precisar para pintar uma parede 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(larg, alt , area))    
tinta = area / 2
print('Para pintar essa parede , Você precisará de {}L de tinta.'.format(tinta))
