''' Método de Gauss 
De forma análoga a anterior, o algoritmo recebe uma matriz completa correspondendo a concatenação da matriz dos coeficientes
com o vetor de termos independentes e retorna o vetor solução no sistema linear.'''

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
            print("Divisão por zero! O sistema é impossível ou indeterminado!") #imprime a mensagem de erro e retorna None
            return None

    return x #retorna o vetor solução

def gauss_simples(matriz):
    #Eliminação gaussiana simples, sem pivoteamento
    #1 passo: Eliminar x1 das equações i = 2,...n. a(11) é o pivô e através dele obtermos multiplicadores m(i1) = a(i1)(0)/a(11)(0)
    n = len(matriz)
    vetor_solucao = [0]*n

    for k in range(n-1): #K é a Etapa em que se elimina a variável X(k) das equações k+1, k+2, ..., n. Vai até n-1 pois Xn já estará isolado
        pivo = matriz[k][k] 
        for i in range(k+1, n): #i é o iterador das linhas. Para cada etapa, as linhas k+1, k+2, ..., n serão alteradas para zerar os coef de Xk
            m = matriz[i][k]/pivo
            matriz[i][k]=0
            for j in range(k+1, n+1): #j é o iterador das colunas, dentro do loop das linhas. o loop vai até n+1 pois deve englobar também os termos independentes
                matriz[i][j] = matriz[i][j] - m*matriz[k][j] #para cada linha i, cada elemento aij deve ser alterado conforme o multiplicador

    vetor_solucao = res_sist_triang_superior(matriz)
    
    return vetor_solucao

def vetor_residuo(matriz, x):
    r = [0]*len(matriz) #vetor resíduo

    for i in range(len(matriz)):
        r[i] = matriz[i][-1] - sum([matriz[i][j]*x[j] for j in range(len(matriz))]) #calcula vetor resíduo r = b - Ax, com b = matriz[i][-1] (ultima coluna da matriz)

    return r

def aplica_metodo(matriz):
    try:
        print("Matriz ok. Solução: ", gauss_simples(matriz))
        print("Vetor resíduo: ", vetor_residuo(matriz, gauss_simples(matriz)))
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

'''#Testes simples. Perceba que funciona.
m = [[2, 3, -1, 5], [4, 4, -3, 3], [2, -3, 1, -1]]
n = [[1, 1, 2, 4], [2, -1, -1, 0], [1, -1, -1, -1]]
print(gauss_simples(m))
print("")
print(gauss_simples(n))
'''

'''test = [[8.7, 3.0, 9.3, 11, 16.4],[24.5, -8.8, 11.5, -45.1, -49.7],[52.3, -84.0, -23.5, 11.4, -80.8],[21.0, -81.0, -13.2, 21.5, -106.3]]
t = print(gauss_simples(test))
vetor_residuo(test, t)'''

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






