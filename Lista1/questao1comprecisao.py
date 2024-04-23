import math

def fatorial(n): #função para calcular o fatorial de um número, recebe n como parâmetro
    if n == 0:
        return 1 #fatorial de 0 é 1
    else:
        return n * fatorial(n-1) #retorna fatorial de n

def e_ex(x, precisao): #função para calcular o valor de e^x, recebe x e n como parâmetros
    e = 0
    n = 0
    termo = 1
    while abs(termo) >= 10 ** (-precisao):
        termo = x**n / fatorial(n)
        e += termo
        n += 1
    return e #retorna o valor de e^x

print("Esse programa serve para calcular aproximações de e^x para n termos da soma de Taylor. No final, será mostrado o valor exato de e^x.")
print("Valor aproximado: ", e_ex(1, 5), " valor exato: ", math.exp(1))