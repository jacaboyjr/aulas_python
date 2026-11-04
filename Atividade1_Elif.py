"""
Crie um programa que recebe 3 notas de um aluno, 
calcula a média dessas provas,
e então utiliza comandos condicionais encadeados para jogar na tela se o aluno foi
Reprovado (média menor que 5), Aprovado ou se ele teve a Nota Perfeita (tirou nota 10 três vezes).

Dica:
Use Variáveis, Input, Print, Float, 1 IF, 1 ELIF, 1 Else
"""

nota_1 = float(input("Digite a primeira Nota: "))
nota_2 = float(input("Digite a segunda Nota: "))
nota_3 = float(input("Digite a terceira Nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f"Você tirou a nota Máxima: {media}, perfeito parabens !!")
elif media >= 5:
    print(f"Você tirou Nota: {media}, Aprovado !")
else:
    print(f"Você não tirou Nota suficiente: {media}, Reprovado ...")
