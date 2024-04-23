import math

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def sen(x, precisao):
    sen = 0 #inicializa a variável sen como 0
    n = 0 #inicializa a variável n como 0, n representa o número de termos da série e o número de iterações
    termo_atual = x #inicializa a variável termo como x, termo representa o termo atual da série
    sinal = 1 #inicializa a variável sinal como 1, sinal representa o sinal do termo atual

    while abs(termo_atual) >= 10**(-precisao): #enquanto o valor absoluto do termo atual for maior ou igual a 10 elevado a -precisao
        sen += termo_atual 
        n += 1
        sinal *= -1 #muda o sinal do termo atual, garante a oscilação entre positivo e negativo
        termo_atual = (x**(2*n + 1)) / fatorial(2*n + 1) * sinal
    return round(sen, precisao) #retorna o valor do seno de x com precisão de precisao casas decimais

def cos(x, precisao): #analogamente, função para calcular o cosseno de x, recebe x e precisão como parâmetros
    cos = 0
    n = 0
    termo_atual = 1
    sinal = 1

    while abs(termo_atual) >= 10**(-precisao):
        cos += termo_atual
        n += 1
        sinal *= -1
        termo_atual = (x**(2*n)) / fatorial(2*n) * sinal
    return round(cos, precisao)

def calcula_aproximacoes(x, p):
    print("*** Valor de x = ", x, " para ", p, " casas decimais***")
    print(f"→ Aproximação de sen({x}): {sen(x, p)}")
    print(f"→ Aproximação de cos({x}): {cos(x, p)}")
    print(f"Valor exato de sen({x}): ", math.sin(x))
    print(f"Valor exato de cos({x}): ", math.cos(x))
    
print("Esse programa serve para calcular aproximações de sen(x) e cos(x) com p casas decimais de precisão. No final, será mostrado o valor exato de sen(x) e cos(x).")
calcula_aproximacoes(1, 5)
pi = math.pi
calcula_aproximacoes(pi/2, 5)
calcula_aproximacoes(pi, 5)






