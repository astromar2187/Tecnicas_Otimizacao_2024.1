import math

def fatorial(n): #função para calcular o fatorial de um número, recebe n como parâmetro
    if n == 0:
        return 1 #fatorial de 0 é 1
    else:
        return n * fatorial(n-1) #retorna fatorial de n

def e_ex(x, n): #função para calcular o valor de e^x, recebe x e n como parâmetros
    e = 0
    for i in range(n):
        e += x**i / fatorial(i)
    return e #retorna o valor de e^x


print("Esse programa serve para calcular aproximações de e^x para n termos da soma de Taylor. No final, será mostrado o valor exato de e^x.")
for x in [1, 2, 4, 6]: #para x = 1, 2, 4 e 6
    print("*** Valor de x = ", x, " ***") #imprime o valor de x
    for n in [3, 6, 9, 12, 15]: #para n = 3, 6, 9, 12 e 15
        print(f"→ Aproximação de e^{x} para {n} termos: {e_ex(x, n)}") #imprime o valor de e^x para n termos
    print("Valor exato de e^x: ", math.exp(x)) #imprime o valor exato de e^x
    print() #pula uma linha
