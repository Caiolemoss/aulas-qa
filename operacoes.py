import math

valor = float(input("Digite um valor: "))

dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_cubica = math.copysign(abs(valor) ** (1 / 3), valor)

print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Quadrado: {quadrado}")

if valor >= 0:
    print(f"Raiz quadrada: {math.sqrt(valor)}")
else:
    print("Raiz quadrada: não existe nos números reais para valores negativos")

print(f"Raiz cúbica: {raiz_cubica}")
