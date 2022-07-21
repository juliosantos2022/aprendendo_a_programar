altura = float(input('qual é a altura?'))
largura = float(input('qual é a largura?'))
area = altura * largura
print('a parede tem {}x{} e sua area é de {}m'.format(altura, largura, area))
tinta = area / 2
print('para pintar essa parede você precisara de {} litos de tintas'.format(tinta))
