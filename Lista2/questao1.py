'''     Implementar a função res_sist_triang. 
Sistemas triangulares são sistemas de equações lineares onde a matriz dos coeficientes é triangular superior ou inferior.
Os sistemas triangulares determinados são resolvidos por susbtituição retroativa (triang. superior) ou substituição 
progressiva (triang. inferior).

A função res_sist_triang recebe uma matriz completa correspondendo a junção da matriz triangular original 
concatenada com um vetor de termos independentes e retorna a solução do sistema, se existir.
Caso o sistema seja indeterminado ou impossível, a função deve retornar None. 
→ n: Número de elementos no vetor de termos independentes é igual ao número de funções no sistema linear, que também deve ser 
o número de linhas da matriz.
→ m: número de variáveis do sistema, corresponde ao número de colunas da matriz
'''

def analise(matriz):
    # Função para analisar o tipo da matriz
    # 1: Matriz triangular superior
    # 2: Matriz triangular inferior
    # 0: Matriz não triangular
    n = len(matriz)
    m = len(matriz[0])-1
    tipo = 0
    for i in range(n):
        for j in range(m):
            if i > j and matriz[i][j] != 0:
                tipo = 2
            elif i < j and matriz[i][j] != 0:
                tipo = 1
    return tipo

#Função substituída por aplica_metodo
'''def res_sist_triang(matriz):
    # Função para resolver sistemas triangulares, chamando a função analise para verificar o tipo da matriz e chamar a função correspodente
    #imprimir a matriz para visualização
    for i in matriz:
        print(i)

    tipo = analise(matriz)
    if tipo == 1:
        print("Sistema triangular superior!")
        print("Método de substituição retroativa")
        print("Resolvendo o sistema... Solução: ", res_sist_triang_superior(matriz))
        print("")
        return 
    elif tipo == 2:
        print("Sistema triangular inferior!")
        print("Método de substituição progressiva")
        print("Resolvendo o sistema... Solução: ", res_sist_triang_inferior(matriz))
        print("")
        return 
    else:
        print("Sistema não é triangular!")
        return None'''

def res_sist_triang_superior(matriz):
    # Método de substituição retroativa
    n=len(matriz) #numero de linhas da matriz
    im = n - 1 #indice de localização na matriz, é igual ao número de linhas - 1 pois a contagem começa em 0 
    x=[0]*(n) #vetor solução inicializado com zeros e com tamanho n (deve ter o tamanho do número de linhas da matriz)
    
    #calcula o valor da última variável xn = bn/an,n (usaremos o indice da matriz da matriz (im) para facilitar a compreensão)
    x[im] = matriz[im][im+1] / matriz[im][im] #valor da última variável x[n] = b[n]/a[n][n]
    #print(f"x[{im+1}] = {x[im]}") #imprime o valor da última variável calculada

    #laço para calcular os valores das variáveis restantes
    for i in range(im-1, -1, -1): #para i variando de im-1 até 0, com passo -1 (perceba que a contagem deve ser decrescente, pois a resolução é retroativa)
        soma = 0 #variável para armazenar a soma dos valores já calculados multiplicados pelos coeficientes da matriz
        for j in range(i+1,im+1): #para j variando de i+1 até im+1 (n), o valor de j deve ser maior que i para que a soma seja feita corretamente
            soma += matriz[i][j]*x[j] #soma é ascrescida dos valores já calculados multiplicados pelos coeficientes da matriz
        
        try: #tratamento de exceção para divisão por zero, evita que o programa pare de funcionar caso ocorra uma divisão por zero
            x[i] = (matriz[i][im+1] - soma) / matriz[i][i] #calcula o valor da variável x[i] = (bi - soma)/ai,i
        except ZeroDivisionError: #exceção para divisão por zero
            print("Divisão por zero! O sistema é impossível ou indeterminado!") #imprime a mensagem de erro e retorna None
            return None
        #print(f"x[{i+1}] = {x[i]}")

    return x #retorna o vetor solução


def res_sist_triang_inferior(matriz):
    # Método de substituição progressiva, de forma análoga ao método de substituição retroativa
    n=len(matriz) #numero de linhas da matriz
    im = n - 1 #indice de localização na matriz, é igual ao número de linhas - 1 pois a contagem começa em 0
    x=[0]*(n) #vetor solução inicializado com zeros e com tamanho n (deve ter o tamanho do número de linhas da matriz)
    
    #calcula o valor da primeira variável x1 = b1/a1,1 (usaremos o indice da matriz da matriz (im) para facilitar a compreensão)
    x[0] = matriz[0][im+1] / matriz[0][0] #valor da primeira variável x1 = b1/a1,1 (perceba que os índices da matriz são im e im+1, respectivamente)
    #print(f"x[1] = {x[0]}") #imprime o valor da primeira variável calculada

    #laço para calcular os valores das variáveis restantes
    for i in range(1,n): #para i variando de 1 até n
        soma = 0 #variável para armazenar a soma dos valores já calculados multiplicados pelos coeficientes da matriz
        for j in range(i): #para j variando de 0 até i, o valor de j deve ser menor que i para que a soma seja feita corretamente
            soma += matriz[i][j]*x[j] #soma é ascrescida dos valores já calculados multiplicados pelos coeficientes da matriz
        try: #tratamento de exceção para divisão por zero, evita que o programa pare de funcionar caso ocorra uma divisão por zero
            x[i] = (matriz[i][im+1] - soma) / matriz[i][i] #calcula o valor da variável x[i] = (bi - soma)/ai,i
        except ZeroDivisionError: #exceção para divisão por zero
            print("Divisão por zero! O sistema é impossível ou indeterminado!") #imprime a mensagem de erro e retorna None
            return None
        #print(f"x[{i+1}] = {x[i]}")

    return x #retorna o vetor solução

def vetor_residuo(matriz, x):
    n = len(matriz)
    r = [0]*len(matriz) #vetor resíduo

    for i in range(n):
        soma = 0
        for j in range(n):
            soma += matriz[i][j]*x[j]
        r[i] = matriz[i][n] - soma

    return r

def aplica_metodo(matriz):
    try:
        tipo = analise(matriz)
        if tipo == 1:
            x = res_sist_triang_superior(matriz)
            print("Sistema triangular superior!")
            print("Método de substituição retroativa")
            print("Resolvendo o sistema... Solução: ", x)
            if x != None:
                print("Vetor resíduo: ", vetor_residuo(matriz, x))
            print("")
            return x
        elif tipo == 2:
            x = res_sist_triang_inferior(matriz)
            print("Sistema triangular inferior!")
            print("Método de substituição progressiva")
            print("Resolvendo o sistema... Solução: ", x)
            if x != None:
                print("Vetor resíduo: ", vetor_residuo(matriz, x))
            print("")
            return x
        else:
            print("Sistema não é triangular!")
            return None
    except ZeroDivisionError:
        print("Erro na matriz. Divisão por zero!")

'''# Teste da função res_sist_triang_superior, com [linha][coluna], vetor solução esperado: [1, -1, 2, 1]
matriz = [[3, 4, -5, 1, -10], [0, 1, 1, -2, -1], [0, 0, 4, -5, 3], [0, 0, 0, 2, 2]]
res_sist_triang(matriz)
# Teste da função res_sist_triang_inferior, com [linha][coluna], vetor solução esperado: [1, -1, 2, 1]
matriz2 = [[2, 0, 0, 0, 2], [-5, 4, 0, 0, 3], [-2, 1, 1, 0, -1], [1, -5, 4, 3, -10]]
res_sist_triang(matriz2)'''



# Testes com as questões da lista
matrizI = [[1, 3, -2, 7, 0, -9, 6, -1, 6.25], [0, 4, 3, -1, 8, 6, -7, 4, 55.08], [0, 0, 7, 4, 2, -4, -8, 2, -2.454], [0, 0, 0, -3, 5, 9, 5, 1, 51.442], [0, 0, 0, 0, 2, -6, -4, 8, 0.000], [0, 0, 0, 0, 0, -5, 0, 3, -0.008], [0, 0, 0, 0, 0, 0, 9, 5, 7.228], [0, 0, 0, 0, 0, 0, 0, 6, 24]]
matrizII = [[1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, -1], [2, 1, 3, 0, 0, 0], [1, 1, 1, 0, 0, -1], [1, -1, 1, -1, 1, 3]]
matrizIII = [[1, 0, 0, 0, 1], [1, 1, 0, 0, -1], [1, 1, 1, 0, 3], [1, 1, 1, 1, 3],]

print("Matriz I:")
aplica_metodo(matrizI)
print("Matriz II:")
aplica_metodo(matrizII)
print("Matriz III:")
aplica_metodo(matrizIII)

