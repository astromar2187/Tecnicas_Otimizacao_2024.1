import time

def soma(n):
    soma = 0
    for i in range(n):
        soma += i
    #print(f"Soma de {n} termos. Resultado: {soma}.")

def multiplicacao(n):
    multiplicacao = 1
    for i in range(1, n+1):
        multiplicacao *= i
    #print(f"multiplicação de {n} termos. Resultado: {multiplicacao}.")

def calculatempo(opcao, n):
    # Marca o tempo de início
    inicio = time.time()

    # Chama a função que você deseja medir o tempo de execução
    if opcao == "soma":
        soma(n)
    if opcao == "multiplicacao":
        multiplicacao(n)

    # Marca o tempo de término
    fim = time.time()

    # Calcula o tempo de execução
    tempo_execucao = fim - inicio
    print(f"Operação: {opcao} de {n} termos. Tempo de execução: {tempo_execucao} segundos")

# Chama a função calculatempo passando a opção e o número de termos
#calculatempo("soma", 1000000)
#calculatempo("soma", 10000000)
calculatempo("multiplicacao", 10000)
calculatempo("multiplicacao", 20000)
calculatempo("multiplicacao", 1000000)

