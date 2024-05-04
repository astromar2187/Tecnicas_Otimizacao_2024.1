'''
O método de Newton é um método iterativo para encontrar raízes de funções.
Este programa implementa um algoritmo para o método de Newton. 
As entradas são a expresão analítica da função f(x) em questão, expressão analítica da primeira derivada dessa função f'(x), expressão 
analítica da segunda derivada da questão f''(x), um intervalo [a,b], contendo uma e só uma raiz real de f(x), o número máximo de iterações M e 
a tolerância E.


Os dados da saída devem ser exibidos de forma tabular, compreendendo:
Sequência de intervalos obtidos durante a execução do método de Newton;
Sequência de aproximações sucessivas (termos iterados);
Imagem da função relativa a cada aproximação;
Sequência de valores relativos ao cálculo da verificação do critério de parada E=abs(x(k+1)-x(k));

Complementarmente, os dados de saída devem incluir:
→ Número de iterações realizadas;
→ Zero da função f(x) encontrado, x*;
→ Imagem da função no ponto x*;
'''

import math

'''Criar uma lista de dicionários para armazenar os valores de f(x), f'(x) e f''(x) para cada função da lista, identificadas de 1 a 10. 
As expressões lambda permitem que você defina a função de forma anônima e, posteriormente, pode ser chamada com um valor de x específico 
para calcular o valor da função nesse ponto.
'''
funcoes = [
    {
        "id": 1,
        "fx": lambda x: x**2 - math.sin(x),
        "f'x": lambda x: 2*x - math.cos(x),
        "f''x": lambda x: 2 + math.sin(x)
    },
    {
        "id": 2,
        "fx": lambda x: 3*x**3-76*x**2+163*x-46,
        "f'x": lambda x: 9*x**2-152*x+163,
        "f''x": lambda x: 18*x-152
    },
    {
        "id": 3,
        "fx": lambda x: x**2+math.log(x),
        "f'x": lambda x: 2*x + 1/x,
        "f''x": lambda x: 2 - 1/x**2
    },
    {
        "id": 4,
        "fx": lambda x: math.cos(x) - x,
        "f'x": lambda x: -math.sin(x) - 1,
        "f''x": lambda x: -math.cos(x)
    },
    '''{


        "id": 5,
        "fx": lambda x: ,
        "f'x": lambda x: ,
        "f''x": lambda x: 
    },
    {
        "id": 6,
        "fx": lambda x: ,
        "f'x": lambda x: ,
        "f''x": lambda x: 
    },
    {
        "id": 7,
        "fx": lambda x:,
        "f'x": lambda x:,
        "f''x": lambda x: 
    },
    {
        "id": 8,
        "fx": lambda x: ,
        "f'x": lambda x: ,
        "f''x": lambda x: 
    },
    {
        "id": 9,
        "fx": lambda x: ,
        "f'x": lambda x: ,
        "f''x": lambda x:
    },
    {
        "id": 10,
        "fx": lambda x: ,
        "f'x": lambda x: ,
        "f''x": lambda x: 
    },'''
]

def analise_intervalo(fx, f_duas_linha_x, a, b):
    if fx(a)*f_duas_linha_x(a) > 0:
        return a
    elif fx(b)*f_duas_linha_x(b) > 0:
        return b
    else:
        print("Intervalo inválido")

def newton(f, f_linha, f_duas_linha, a, b, M, E):
    k = 0
    x = [0]*M
    x[0] = analise_intervalo(f, f_duas_linha, a, b)

    while(k < M):
        k+=1
        x[k] = x[k-1] - f(x[k-1])/f_linha(x[k-1])

        print(f"k = {k}:")
        print(f"x{k-1} - f(x{k-1}) = x{k}")
        print(f"{x[k-1]} - {f(x[k-1])} = {x[k]}")

        if abs(x[k]-x[k-1]) < 0.0001:
            break
        
    return x[k]

newton(funcoes[0]["fx"], funcoes[0]["f'x"], funcoes[0]["f''x"], 0, 1, 100, 0.0001)


