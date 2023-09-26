print("*** Lab - Bem-vindo à Calculadora Python ***")
print("Selecione a opção desejada: \n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

operacao = int(input("Digite a operação desejada (1/2/3/4): "))
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

if operacao == 1:
  strOperacao = " + "
  resultado = primeiroNumero + segundoNumero
elif operacao == 2:
  strOperacao = " - "
  resultado = primeiroNumero - segundoNumero
elif operacao == 3:
  strOperacao = " * "
  resultado = primeiroNumero * segundoNumero
elif operacao == 4:
  strOperacao = " / "
  resultado = primeiroNumero / segundoNumero
else:
  print("Operação inválida!")

print(str(primeiroNumero) + strOperacao + str(segundoNumero) + " = " + str(resultado))