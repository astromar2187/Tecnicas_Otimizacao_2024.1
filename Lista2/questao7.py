'''O seguinte programa verificação da convergência pelo critério das linhas e critério das colunas de um sistema linear visando 
a resolução por meio de um método iterativo (Método de Jacobi).
A função principal recebe como argumentos a matriz dos coeficientes e o vetor dos termos independentes, concatenados (matriz) e retorna
i) Status do critério das linhas (verdadeiro/falso) e ii) Status do critério das colunas (verdadeiro/falso).

O teorema do critério das linhas versa que seja o sistama Ax = b e seja a(k)={sum de j=1 a n, com j dif de k {(A[k][j])}/A[k][k]}, 
se a = max(a(k)){para 1<=k<=n} < 1, o método de Gauss-Jacobi gera uma sequência convergente para a solução do sistema, independente da 
escolha da aproximação inicial, x0.

Já o teorema do critério das colunas versa que seja o sistama Ax = b, definimos: i) B[1] = sum de j=2 a n (A[j][1])/A[1][1],

Aqui, implementei estritamente conforme os teorema, mas há formas de otimizar essa verificação, a fim de diminuir o esforço comp. necessário,
principalemente para matrizes de grande porte. Para o criterio das linhas, por exemplo, a ideia seria invés de montar o vetor (a) completamente e 
depois testar o valor max dele, implementar um loop que verifica se a = sum(matriz[k][j] for j in range(n) if j != k)/matriz[k][k] < 1 e caso o teste 
retorne falso, o laço seria interrompido sem a necessidade de verificar e somar n-1 elementos de cada uma das n linhas da matriz.'''

def criterio_linhas(matriz):
    n = len(matriz)
    a=[0]*n #Inicializando um vetor para guardar ak

    for k in range(n):
        a[k] = sum(matriz[k][j] for j in range(n) if j != k)/matriz[k][k]

    return max(a) < 1 #Retorna True se o valor máximo é menor que 1, ou seja, se a condição de convergência é atendida e False caso contrário

def criterio_sassenfeld(matriz):
    n = len(matriz)
    b=[0]*n #Inicializando um vetor para guardar bk

    for k in range(n):
        b[k] = sum(matriz[j][k] for j in range(n) if j != k)/matriz[k][k]
    

    return max(b) < 1 #Retorna True se o valor máximo é menor que 1, ou seja, se a condição de convergência é atendida e False caso contrário

def verifica_matriz(matriz):
    return criterio_linhas(matriz), criterio_colunas(matriz)

def aplica_metodo(matriz):
    try:
        status_linhas, status_colunas = verifica_matriz(matriz)
        print("Matriz ok. Status Critério das linhas: ", status_linhas)
        print("Matriz ok. Status Critério das colunas: ", status_colunas)
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

'''teste = [[10, 2, 1, 7],[1, 5, 1, -8], [2, 3, 10, 6]]
verifica_matriz(teste)'''

#Exemplos da lista
matrizI = [[10, 1, 1, 2, 3, -2, 6.57], [4, -20, 3, 2, -1, 7, -68.448], [5, -3, 15, -1, -4, 1,-112.05], [-1, 1, 2, 8, -1, 2, -3.968], [1, 2, 1, 3, 9, -1, -2.18], [-4, 3, 1, 2, -1, 12, 10.882]]
matrizII = [[3, 3, 1, 7], [2, 2, -1, 3], [1, -1, 5, 5]]
#Matriz esparsa é uma matriz que possui mais elementos nulos do que não nulos
#matrizIII = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 2], [1, 0, 1, 0, 2], [0, 0, 0, 1, 1]]

print("Matriz I")
aplica_metodo(matrizI)
print("Matriz I")
aplica_metodo(matrizII)
'''print("Matriz I")
aplica_metodo(matrizIII)'''