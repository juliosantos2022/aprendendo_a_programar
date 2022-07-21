preço = float(input('qual o preço do produto?R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava {:.2f}reais com o desconto de 5% vai custar {:.2f}reais'.format(preço, novo))

