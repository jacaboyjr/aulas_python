"""
A (9 a 10)
B (8 a 8.9)
C (7 a 7.9)
D (6 a 6.9)
F (Menor que 6)
"""

nota_1 = float(input("Digite a primeira Nota (0 - 10): "))
if nota_1 > 10:
    print("Você digitou um numero maior que 10, será considerado NOTA = 10")
    nota_1 = 10
elif nota_1 < 0:
    print("Você digitou um numero negativo, será considerado NOTA = 0")
    nota_1 = 0
nota_2 = float(input("Digite a segunda Nota (0 - 10): "))
if nota_2 > 10:
    print("Você digitou um numero maior que 10, será considerado NOTA = 10")
    nota_2 = 10
elif nota_2 < 0:
    print("Você digitou um numero negativo, será considerado NOTA = 0")
    nota_2 = 0
nota_3 = float(input("Digite a terceira Nota (0 - 10):  "))
if nota_3 > 10:
    print("Você digitou um numero maior que 10, será considerado NOTA = 10")
    nota_3 = 10
elif nota_3 < 0:
    print("Você digitou um numero negativo, será considerado NOTA = 0")
    nota_3 = 0

media = (nota_1 + nota_2 + nota_3) / 3
media = round(media, 2)


if media == 10:
    print(f"Você tirou a nota Máxima: {media} e nota 'A', perfeito parabens !!")
elif media >= 9:
    print(f"Você tirou Nota: {media} e nota 'A', Aprovado !")
elif media >= 8:
    print(f"Você tirou Nota: {media} e nota 'B', Aprovado !")
elif media >= 7:
    print(f"Você tirou Nota: {media} e nota 'C', Aprovado !")
elif media >= 6:
    print(f"Você tirou Nota: {media} e nota 'D', Aprovado !")
elif media >= 5:
    print(f"Você tirou Nota: {media} e nota 'F', Aprovado !")
else:
    print(f"Você não tirou Nota suficiente: {media} e nota 'F', Reprovado ...")


"""
A (9 a 10)
B (8 a 8.9)
C (7 a 7.9)
D (6 a 6.9)
F (Menor que 6)
"""
