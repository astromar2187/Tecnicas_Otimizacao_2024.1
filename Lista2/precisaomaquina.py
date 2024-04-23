'''A precisão da máquina é definida como sendo o menor número positivo E tal que 1 + E > 1. Este número depende 
totalmente do sistema de representação utilizado. Este algoritmo estima a precisão da máquina.'''

def precisao_float():
    A = float(1)
    s = float(2)

    while(s>1):
        A=A/2
        s=1+A
    
    return 2*A

print("Precisão:", precisao_float())