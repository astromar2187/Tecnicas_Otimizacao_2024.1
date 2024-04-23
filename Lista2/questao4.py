''' Método de Jordan 
De forma análoga a anterior, o algoritmo recebe uma matriz completa correspondendo a concatenação da matriz dos coeficientes
com o vetor de termos independentes e retorna o vetor solução no sistema linear.'''

def print_matriz(matriz): #para vizualização
    for a in range(len(matriz)):
        print(matriz[a])
    return

def jordan_simples(matriz):
    #Eliminação de Jordan simples, sem pivoteamento
    n = len(matriz)
    vetor_solucao = [0]*n

    for k in range(n): #K é a Etapa em que se elimina a variável X(k) das equações 1, 2, ... k-1, k+1, ... n.
        pivo = matriz[k][k]
        '''print(f"***Etapa {k}. Pivô: {pivo}***")
        print("")'''

        for i in range(n): #i é o iterador das linhas. Para cada etapa, todas as linhas com i diferente de k serão alteradas
            if i != k: #não é necessário alterar a linha k pois ela já está sendo usada como pivô
                '''print("")
                print(f"    Linha {i} antes do processo: {matriz[i]}")
                print(f"    Multiplicador para a linha {i}: {matriz[i][k]}/{pivo}")'''
                m = matriz[i][k]/pivo
                matriz[i][k]=0 #zera o elemento aik
                for j in range(n+1): #j é o iterador das colunas, dentro do loop das linhas. o loop vai até n+1 pois deve englobar também os termos independentes
                    if j != k: #não é necessário alterar o elemento aik pois ele já foi zerado
                        matriz[i][j] = matriz[i][j] - m*matriz[k][j] #para cada linha i, cada elemento aij deve ser alterado conforme o multiplicador
            #print(f"    Linha {i} ao fim do processo: {matriz[i]}")
        
        '''print("")
        print(f"Matriz após a etapa {k}: ")
        print_matriz(matriz)
        print("")'''


    for i in range(n):
        vetor_solucao[i] = matriz[i][n]/matriz[i][i]

    '''print("Matriz após eliminação de Jordan: ")
    print_matriz(matriz)
    print("Vetor solução: ", vetor_solucao)'''
    
    return vetor_solucao

def vetor_residuo(matriz, x):
    r = [0]*len(matriz) #vetor resíduo

    for i in range(len(matriz)):
        r[i] = matriz[i][-1] - sum([matriz[i][j]*x[j] for j in range(len(matriz))]) #calcula vetor resíduo r = b - Ax, com b = matriz[i][-1] (ultima coluna da matriz)

    return r

def aplica_metodo(matriz):
    try:
        x = jordan_simples(matriz)
        print("Matriz ok. Solução: ", x)
        print("Vetor resíduo: ", vetor_residuo(matriz, x))
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

#Testes simples. Perceba que funciona.
'''m = [[1, 1, 2, 4], [2, -1, -1, 0], [1, -1, -1, -1]]
print_matriz(m)
jordan_simples(m)'''

#Testes com as questões da lista.
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




