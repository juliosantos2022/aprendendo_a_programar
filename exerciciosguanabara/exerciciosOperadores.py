n1 = int(input('digite um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m , d), end=' ')
print('divisão inteira {} e potência {}'.format(di, e))
