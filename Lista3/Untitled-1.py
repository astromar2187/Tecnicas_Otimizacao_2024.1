'''Usado na questão 08 dos exercícios de fixação da lista 03. Somente para auxiliar nos cálculos, diminuindo
os erros de cálculo manual. Não é necessário para a resolução da questão.'''


import math
def f(x):
    res = (x**2 - math.sin(x))/(2*x - math.cos(x))
    return res

def newton(x0):
    k = 0
    x = [0]*100
    x[0] = x0

    while(k<100):
        k+=1
        x[k] = x[k-1] - f(x[k-1])

        print(f"k = {k}:")
        print(f"x{k-1} - f(x{k-1}) = x{k}")
        print(f"{x[k-1]} - {f(x[k-1])} = {x[k]}")

        if abs(x[k]-x[k-1]) < 0.0001:
            break

newton(1)



