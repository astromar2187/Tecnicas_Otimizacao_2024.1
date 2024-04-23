import matplotlib.pyplot as plt

def populacaoA(ano):
    return 100000 * ((1.01) ** (ano-2020))

def populacaoB(ano):
    return 30000 * ((1.03) ** (ano-2020))


'''print("População da cidade A em 2025:", populacaoA(2025))
print("População da cidade B em 2025:", populacaoB(2025))'''

# Dados das cidades
anos = list(range(2020, 2100))
populacao_A = [populacaoA(ano) for ano in anos]
populacao_B = [populacaoB(ano) for ano in anos]

# Cálculo do ano em que a população de B ultrapassa a população de A
ano = 2020
A = populacaoA(ano)
B = populacaoB(ano)
while B <= A:
    ano += 1
    A = populacaoA(ano)
    B = populacaoB(ano)
print(f"Em {ano} a população de B ultrapassará a população de A. A população de A será de {A} e a população de B será de {B}.")

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.plot(anos, populacao_A, label='Cidade A')
plt.plot(anos, populacao_B, label='Cidade B')
plt.axvline(ano, color='r', linestyle='--', label=f'População de B ultrapassa a de A em {ano}')
plt.title('Crescimento da População ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('População')
plt.legend()
plt.grid(True)
plt.show()
