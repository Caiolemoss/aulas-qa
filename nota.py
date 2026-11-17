nome = input("Digite seu nome: ")
nota1 = float(input("Digita sua primeira nota: "))
nota2 = float(input("Digita sua segunda nota: "))
nota3 = float(input("Digita sua terceira nota: "))
nota4 = float(input("Digita sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"{nome}, sua média é: {media}")

if media >= 6:
    print(f"Parabéns, {nome}! Você foi aprovado!")
else:
    print(f"Você foi reprovado, {nome}.")