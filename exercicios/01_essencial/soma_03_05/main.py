def resposta(n):
    soma = 0
    for numero in range(n):
        if numero % 3 == 0 or numero % 5 == 0:
            soma += numero
    return soma
