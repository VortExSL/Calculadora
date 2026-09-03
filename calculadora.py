while True:
  print("\n-- testando calculadora! --")
  print("1. adiçao (+)")
  print("2. subtraçao (-)")
  print("3. multiplicaçao (*)")
  print("4. divisao (/)")
  print("5. mete o pé")

  P = input("escolha uma opçao (1-5): ")

  if P == '5' :
     print("metendo o pé daqui adeus!")
     break

  if P in ['1', '2', '3', '4']:
   num1 = float(input("Digite o primeiro numero: "))
   num2 = float(input("Digite o segundo numero: "))

   if P == '1':
     resultado = num1 + num2
     print(f"Resultado: {num1} + {num2} = {resultado}")
   elif P == '2':
     resultado = num1 - num2
     print(f"Resultado: {num1} - {num2} = {resultado}")
   elif P == '3':
     resultado = num1 * num2
     print(f"Resultado: {num1} * {num2} = {resultado}")
   elif P == '4':
     if num2 != 0:
      resultado = num1 / num2
      print(f"Resultado: {num1} / {num2} = {resultado}")
