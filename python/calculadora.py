print ("===Calculadora Python===")

numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    if numero2 !=0:
        resultado = numero1 / numero2
    else:
        resultado = "Não é possível realizar divisão por zero."

else:
    resultado = "Operação inválida."

print("Resultado:", resultado)