'''
VERSAO BETA

Embora o método de Gauss seja exato matematicamente, ele pode ser bastante sensível a erros de arredondamento da máquina. Isso ocorre 
porque computadores operam com uma precisão finita e, portanto, não podem representar números reais com precisão infinita. Assim, erros de 
arredondamento podem comprometer o resultado obtido pelo algoritmo computacional. O "tamanho" do erro depende de vários fatores de hardware
e software e, portanto, diferentes máquinas podem apresentar medidas diferentes de erro. Para calcular a precisão da sua máquina, você pode 
utilizar o algoritmo disposto em precisaomaquina.py.
O refinamento de soluções é uma técnica utilizada para minimizar esses erros de arredondamento.

Neste procedimento, consideramos xa uma solução aproximada obtida pelo método de Gauss para um sistema linear Ax=b cuja solução é o vetor x. 
Se xa é uma solução aproximada, então existe c tal que x = xa + c, onde c é o vetor de correção. Assim:
Se substituirmos xa na equação Ax=b, obtemos que Ac = b - Axa. Podemos obter c resolvendo o SL Ac = r, onde r é chamado de >>resíduo<<.
Ac =r pode ser resolvido de forma análoga ao método de Gauss.

Para refinar uma solução qualquer xa, repetimos o processo de eliminação gaussiana para resolver o sistema Ac = r, até que o vetor solução xa seja 
igual a x ou até que o erro seja suficientemente pequeno, o que definiremos depois.
O código a seguir implementa o refinamento de soluções para um sistema linear Ax=b. A função refinamento recebe a matriz A concatenada com o vetor b 
e a solução inicial xa. Ela retorna a solução refinada x, ou None caso não seja possível realizar o procedimento.
'''

def print_matriz(matriz): #teste
    for a in range(len(matriz)):
        print(matriz[a])
    return 
 
def res_sist_triang_superior(matriz):
    n=len(matriz) 
    #im = n - 1 #indice de localização na matriz, é igual ao número de linhas - 1 pois a contagem começa em 0 
    x=[0]*(n) 
    
    x[im] = matriz[im][im+1] / matriz[im][im] 
    try:
        for i in range(n-1, -1, -1):
            soma = sum(matriz[i][j] * x[j] for j in range(i+1, n))
            x[i] = (matriz[i][n] - soma) / matriz[i][i]
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
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

def refinamento(matriz, xa):
    x = xa
    r = [0]*len(matriz) #vetor resíduo

    for i in range(3): #max de iterações
        vetor_residuo(matriz, x)
    
        r = [r[i]/matriz[i][i] for i in range(len(matriz))] #atualiza vetor resíduo
        matriz_correcao = [matriz[i][:-1]+[r[i]] for i in range(len(matriz))]
        try:
            c = gauss_simples(matriz_correcao) #resolve sistema Ac = r
            if c == None:
                return None
            x = [x[j] + c[j] for j in range(len(x))] #atualiza vetor solução

        except:
            print("Erro na resolução do sistema Ac = r")
            return None

        
    return x

matrizII = [[8.7, 3, 9.3, 11, 16.4], [24.5, -8.8, 11.5, -45.1, -49.7], [52.3, -84, -23.5, 11.4, -80.8], [21, -81, 13.2, 21.5, -106.3]]
try:
    print("Matriz II ok. Solução sem refinamento: ", gauss_simples(matrizII))
    print("Solução refinada: ", refinamento(matrizII, gauss_simples(matrizII)))
except:
    print("Outro erro na matriz II")