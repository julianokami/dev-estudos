print("===Média de Aluno===")

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a primeira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Parabéns você foi aprovado!:) Sua média foi:", media)

elif media >= 5:
    print("Você está em recuperação, sua media foi:", media,"tente novamente :(")

else:
    print("Sinto muito você foi reprovado, sua média foi:", media)