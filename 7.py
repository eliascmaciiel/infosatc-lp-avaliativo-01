print ("Olá, nesse script você deverá apresentar uma temperatura em graus Fahrenheit e iremos lhe retornar um valor em Celsius.")

temp1 = float(input("Digite uma temperatura em graus Fahrenheit: "))

temp2 = 5 * (temp1 - 32) / 9

print("A temperatura digitada em Fahrenheit foi: {}, ela convertira em Celsius é: {} ".format(temp1,temp2))