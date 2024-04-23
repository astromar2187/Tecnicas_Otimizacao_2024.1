'''
O pivoteamento total é uma técnica mais refinada que o pivoteamento parcial. Nela, a cada etapa k, escolhemos a linha i e a coluna j 
tal que |a(ij)| é o maior possível e trocamos a linha k pela linha i e a coluna k pela coluna j, garantindo que a11 seja o maior 
possível. A função pivoteamento_total implementa essa técnica.

Note que uma operação a mais precisa ser feita nesse caso, pois no pivoteamento total as colunas da matriz original também são trocadas,
o que implica que da forma em que o vetor solução é calculado na função res_sist_triang_superior, ele não será mais válido, pois se, por exemplo,
as colunas a e b forem trocadas, a posição a do vetor x não conterá mais o valor de xa, mas sim de xb e vice e versa. 
Portanto, a função troca_colunas foi implementada para trocar as colunas da matriz, de forma que o vetor solução seja calculado corretamente.
Além dessa mudança, a função pivoteamento_total acrescenta uma lista p, que guarda a ordem das colunas trocadas, para que o vetor solução seja 
calculado corretamente, a partir da permutação das soluções correpondetes as colunas trocadas. 
'''

def troca_linhas(matriz, lin1, lin2):
    aux = matriz[lin1]
    matriz[lin1]=matriz[lin2]
    matriz[lin2]=aux
    return matriz

def troca_colunas(matriz, col1, col2):
    for i in range(len(matriz)):
        aux = matriz[i][col1]
        matriz[i][col1] = matriz[i][col2]
        matriz[i][col2] = aux
    return matriz

def print_matriz(matriz): #teste
    for a in range(len(matriz)):
        print(matriz[a])
    return 

def res_sist_triang_superior(matriz):
    n=len(matriz) 
    im = n - 1 #indice de localização na matriz, é igual ao número de linhas - 1 pois a contagem começa em 0 
    x=[0]*(n) 
    
    x[im] = matriz[im][im+1] / matriz[im][im] 

    for i in range(im-1, -1, -1): 
        soma = 0 
        for j in range(i+1,im+1): 
            soma += matriz[i][j]*x[j]
        
        try: 
            x[i] = (matriz[i][im+1] - soma) / matriz[i][i] 
        except ZeroDivisionError: 
            print("Divisão por zero!") #imprime a mensagem de erro e retorna None
            return None

    return x #retorna o vetor solução

def pivoteamento_total(matriz):
    n = len(matriz)
    p = list(range(n)) #lista que guarda a ordem das colunas trocadas, inicialmente é [0, 1, 2, ..., n-1], ou seja, a ordem original
    for k in range(n-1):
        maior = 0
        for i in range(k, n):
            for j in range(k, n):
                if abs(matriz[i][j]) > maior:
                    maior = abs(matriz[i][j])
                    linha = i
                    coluna = j
        matriz = troca_linhas(matriz, k, linha)
        matriz = troca_colunas(matriz, k, coluna)
        p[k], p[coluna] = p[coluna], p[k] #troca a ordem das colunas na lista p
        #print_matriz(matriz)
        for i in range(k+1, n):
            m = matriz[i][k]/matriz[k][k]
            for j in range(k, n+1):
                matriz[i][j] = matriz[i][j] - m*matriz[k][j]
    return matriz, p

def gauss_piv_total(matriz):
    n = len(matriz)
    matriz, p = pivoteamento_total(matriz)
    if matriz is None:
        return None
    else:
        x = res_sist_triang_superior(matriz)
        return [x[i] for i in p] #retorna o vetor solução permutado de acordo com a ordem das colunas trocadas

def vetor_residuo(matriz, x):
    r = [0]*len(matriz) #vetor resíduo

    for i in range(len(matriz)):
        r[i] = matriz[i][-1] - sum([matriz[i][j]*x[j] for j in range(len(matriz))]) #calcula vetor resíduo r = b - Ax, com b = matriz[i][-1] (ultima coluna da matriz)

    return r

def aplica_metodo(matriz):
    try:
        x = gauss_piv_total(matriz)
        print("Matriz ok. Solução: ", x)
        print("Vetor resíduo: ", vetor_residuo(matriz, x))
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

#Testes com as questões da lista. ALgumas não funcionam. Erro: Divisão por zero (pivô)!
matrizI = [[3, 3, 1, 7], [2, 2, -1, 3], [1, -1, 5, 5]]
matrizII = [[8.7, 3, 9.3, 11, 16.4], [24.5, -8.8, 11.5, -45.1, -49.7], [52.3, -84, -23.5, 11.4, -80.8], [21, -81, 13.2, 21.5, -106.3]]
matrizIII = [[0.8754, 3.0081, 0.9358, 1.1083, 0.8472], [2.4579, 0.8758, 1.1516, -4.5148, 1.1221], [5.2350, -0.8473, -2.3582, 1.1419, 2.5078], [2.1015, 8.1083, 1.3232, 2.1548, -6.4984]]
matrizIV = [[1, 2, 1, 3], [2, 3, 1, 5], [3, 5, 2, 1]]
matrizV = [[1, 1, 2, 4, 7.12], [1, 1, 5, 6, 12.02], [2, 5, 1, 2, 14.9], [4, 6, 2, 1, 20.72]]
matrizVI = [[1, -5, 3, 9, -7, 21, -7, -2, -10.79], [3, 2, -5, 8, 3, -13, 0, 1, -2.14], [2, 1, 9, -6, -6, 8, -3, 3, -130.608], [4, -4, 2, 5, 8, -6, 2, -4, 76.3], [-5, 6, -4, 4, 9, -10, 1, 5, -11.1], [6, 1, 5, -2, 15, 4, -9, 7, 0.135], [0, -9, 1, 1, -12, 2, 10, 8, -3.108], [3, 10, 3, 7, 3, 1, 1, -3, 632,5]]
matrizVII = [[3, 0, -9, 6, 9, 4, -1, -0.108], [-9, 3, 8, 9, -12, 6, 3, 26.24], [1, -9, 1, -3, 1, -5, 5, 92.808], [4, 8, -10, 8, -1, 4, -4, 53.91], [-5, 5, 4, 11, 3, 8, 7, 143.55], [6, -2, 9, -7, -5, -3, 8, -6.048], [8, 7, 2, 5, 2, 1, -3, 137.94]]

print("Matriz I")
aplica_metodo(matrizI)
print("Matriz II")
aplica_metodo(matrizII)
print("Matriz III")
aplica_metodo(matrizIII)
print("Matriz IV")
aplica_metodo(matrizIV)
print("Matriz V")
aplica_metodo(matrizV)
print("Matriz VI")
aplica_metodo(matrizVI)
print("Matriz VII")
aplica_metodo(matrizVII)