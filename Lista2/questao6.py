'''
O seguinte programa implementa o Método de Gauss-Seidel para resolver sistemas lineares.
De forma análoga a anterior, a função principal recebe como argumentos a matriz dos coeficientes e o vetor dos termos independentes 
concatenados (matriz), uma aproximação inicial x0, a tolerância (E) e o número máximo de iterações (M). Os dados de saída são o vetor 
solução melhorada x e o vetor resíduo r.

O método de Gauss-Seidel também é um método iterativo para resolver sistemas lineares. A ideia é a mesma de Jacobi: transformar o sistema 
Ax = b em um sistema equivalente x = Cx+g, onde C é uma matriz de iteração e g é um vetor de iteração, que já foram definidos na questão 06. 
O método consiste em iterar a equação x(j)(k+1) = Cx(k+1, de i=1 a i=j-1 e k para os restantes)+g até que a diferença entre duas iterações 
consecutivas seja menor que a tolerância E ou até que o número máximo de iterações M seja atingido.
'''
def print_matriz(matriz): #teste
    for a in range(len(matriz)):
        print(matriz[a])
    return 

def obter_C_g(matriz): #Continua igual
    #Separação pela diagonal
    n = len(matriz)
    C = [[0]*n for _ in range(n)]  #Matriz C, n*n
    g = [0]*n #Vetor g, n*1

    #Monta C
    for i in range(n): #itera linhas
        for j in range(n): #itera colunas
            if i==j: #zera os elemntos da diagonal
                C[i][j] = 0
            else: #monta os demais elementos
                C[i][j] = -1*matriz[i][j]/matriz[i][i]
        #monta g a partir da ultima coluna da matriz (n), o que corresponde ao vetor independente
        g[i] = matriz[i][-1]/matriz[i][i]

    return C, g


def gauss_seidel(matriz, x0, E, M):
    n = len(matriz)
    C, g = obter_C_g(matriz)
    #x  = [0]*n 
    x = x0.copy()

    # O trecho abaixo calcula x(k+1), com M iterações máximas ou até atingir o critério de parada. 
    for k in range(M): #Iterador de etapas, max M
        for i in range(n): #iterador de linhas
            soma = 0
            for j in range(n): #iterador de colunas
                if i==0 or j>i:
                    soma += C[i][j]*x0[j] #Calcula C*x(k) para j>i (valores desatualizados, x0)
                    '''print(f"+ C[{i}][{j}]*x0[{j}]")
                    print(f"+ {C[i][j]}*{x0[j]}")'''
                elif j<i:
                    soma += C[i][j]*x[j] #Calcula C*x(k) para j<i (valores atualizados, x)
                    '''print(f"+ C[{i}][{j}]*x[{j}]")
                    print(f"+ {C[i][j]}*{x[j]}")'''
            x[i] = soma + g[i] # Faz x(k+1) = C*x(k)+g
            '''print(f"x[{i}] = soma + {g[i]} = {x[i]}")
            print(f"Fim da soma {i}")'''

        print("Fim etapa ", k+1, " x: ", x)
        # O trecho abaixo implementa a verificação do critério de parada
        maior_dif = 0
        maior_x = max(abs(y) for y in x)
        #print("Maior x = ", maior_x)

        #A partir daqui não houve mudança. Teste de condição de parada permanece o mesmo
        for d in range(n):
            if(abs(x[d]-x0[d]) > maior_dif):
                maior_dif = abs(x[d]-x0[d])/maior_x
                #print("Maior dif atual: ", maior_dif)
        if(maior_dif<E):
            print("Condição de parada atingida! Max dif = ", maior_dif)
            break

        x0 = x.copy() #atualiza x(k) = x(k+1), para o calculo de k+1+1
        #print(f"Fim da etapa {k}")

    print(f"Finalizado com {k+1} iterações")
    return x

def vetor_residuo(matriz, x): #Sem alterações
    r = [0]*len(matriz) #vetor resíduo

    for i in range(len(matriz)):
        r[i] = matriz[i][-1] - sum([matriz[i][j]*x[j] for j in range(len(matriz))]) #calcula vetor resíduo r = b - Ax, com b = matriz[i][-1] (ultima coluna da matriz)

    return r


def aplica_metodo(matriz):
    try:
        x0 = [0]*len(matriz)
        x = gauss_seidel(matriz, x0, 0.05, 100)
        print("Matriz ok. Solução: ", x)
        print("Vetor resíduo: ", vetor_residuo(matriz, x))
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

'''#Teste
teste = [[5, 1, 1, 5],[3, 4, 1, 6], [3, 3, 6, 0]]
x0 = [0, 0, 0]
E = 0.0000000000000000001
sol_teste = gauss_seidel(teste, x0, E, 200)
print("Solução: ", sol_teste)
print("Vetor resíduo: ", vetor_residuo(teste, sol_teste))'''

#Exemplos da lista
matrizI = [[10, 1, 1, 2, 3, -2, 6.57], [4, -20, 3, 2, -1, 7, -68.448], [5, -3, 15, -1, -4, 1,-112.05], [-1, 1, 2, 8, -1, 2, -3.968], [1, 2, 1, 3, 9, -1, -2.18], [-4, 3, 1, 2, -1, 12, 10.882]]
matrizII = [[3, 3, 1, 7], [2, 2, -1, 3], [1, -1, 5, 5]]
#Matriz esparsa é uma matriz que possui mais elementos nulos do que não nulos
matrizIII = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 2], [1, 0, 1, 0, 2], [0, 0, 0, 1, 1]]

print("Matriz I")
aplica_metodo(matrizI)
print("Matriz I")
aplica_metodo(matrizII)
print("Matriz I")
aplica_metodo(matrizIII)