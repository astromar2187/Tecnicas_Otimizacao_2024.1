import math

def funcao(x):
    return math.exp(x) - math.sin(x) - 2 # f(x) = e^x - sen(x) - 2

def recorrencia(x_atual):
    x_proximo = x_atual - funcao(x_atual) / (math.exp(x_atual) - math.cos(x_atual)) # x_n+1 = x_n - f(x_n) / f'(x_n)
    return x_proximo

def aproximacao_sucessiva(x_inicial, erro, max_iter):
    x_atual = x_inicial
    i = 0

    while True:
        x_proximo = recorrencia(x_atual) # x_n+1 = x_n - f(x_n) / f'(x_n)
        i += 1
        print("Iteração ", i, ": ", x_proximo) # Printa o valor de x_n+1 a cada iteração, serve apenas para visualização


        if abs(x_proximo - x_atual) <= erro: # |x_n+1 - x_n| <= erro
            break

        if i >= max_iter: # Se o número de iterações for maior que o máximo, encerra o loop: evita loop infinito
            print("Número máximo de iterações alcançado.")
            break

        x_atual = x_proximo # Atualiza o valor de x_n para o próximo valor calculado

    return x_proximo, i

if __name__ == "__main__":
    res, iteracoes = aproximacao_sucessiva(0.5, 1e-5, 10000)
    print("A raiz da equação é aproximadamente: ", res, ". Com ", iteracoes, " iterações.")


