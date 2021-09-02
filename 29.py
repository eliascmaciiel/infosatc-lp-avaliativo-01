print("Olá, seja muito bem vindo, nesse programa iremos calcular sua média baseado em duas notas.")

n1 = float(input("Digite sua primeira nota: "))

n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2)/2

if media >= 7:

   print("Parabéns, você foi aprovado com média {}. ".format(media))

if media >= 5 and media < 7:

   print("Você ficou em recuperação com média {}. ".format(media))

if media < 5:

   print("Infelizmente você foi reprovado com média {}. ".format(media))