# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.

nota = float(input("Digite a nota do aluno: "))


if nota >= 7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")