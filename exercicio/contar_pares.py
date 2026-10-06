def contar_pares(numeros):
    contador = 0
    for n in numeros:
        if n % 2 == 1:
            contador += 1
    return contador

numeros = [2, 4, 6, 7, 9]
print("Quantidade de pares:", contar_pares(numeros))
