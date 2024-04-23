def calcular_polinomio(grau, coeficientes, x):
    res=0;
    for i in range(grau+1):
        res+=coeficientes[i]*(x**(grau-i))
        #print(f"{coeficientes[i]} *(({x}**{grau-i}))")
        #print(res)

    return res


resultado_teste_1 = calcular_polinomio(2, [1, 1, 1], 2)
print("Resultado do polinômio para x̅ =", 2, "é:", resultado_teste_1)

#questão i - Determine P(x) = -x^5+2x^4-5x^3+2x^2+4x-1
resultado_teste_4 = calcular_polinomio(5, [-1, 2, -5, 2, 4,-1], -2)
print("Resultado do polinômio para x̅ =", -2, "é:", resultado_teste_4)

#questão ii - Determine P(x) = 3x^9 + 2x^8 - 10x^7 + 2x^6 -15x^5 - 3x^4 + 2x^3 - 16x^2 + 3x - 5
resultado_teste_5 = calcular_polinomio(9, [3, 2, -10, 2, -15, -3, 2, -16, 3, -5], 2)
print("Resultado do polinômio para x̅ =", 2, "é:", resultado_teste_5)




