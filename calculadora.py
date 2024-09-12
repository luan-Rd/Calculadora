while True:
  numero1 = int(input("Digite o primeiro valor: "))
  operacao1 = input("Digite a operação: ")
  numero2 = int(input("Digite o segundo valor: "))

  if operacao1 == "+":
    valorfinal = numero1 + numero2
  elif operacao1 == "-":
    valorfinal = numero1 - numero2
  elif operacao1 == "*":
    valorfinal = numero1 * numero2
  elif operacao1 == "/":
    valorfinal = numero1 / numero2
  else: valorfinal = "Operação invalida"

  print(numero1, operacao1, numero2,"=", valorfinal )
