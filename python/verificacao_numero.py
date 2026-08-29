print("===Verificação de número===")

numero = int(input("Digite um número para fazer a verificação: "))

if numero > 0:
    print("Esse número é positivo!")

elif numero < 0:
    print("Esse número é negativo!")

else:
    print("O número que você digitou é zero.")

if numero % 2 == 0:
    print("O número", numero, "é par.")

else:
    print("O número", numero, "é impar.")
