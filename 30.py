print("Olá, seja muito bem vindo, nesse programa iremos calcular quantos dólares você teria.")

real = float(input("Digite um valor em R$: "))

cotacao = 5.16

dolar = real / cotacao

print("Você com {} R$ teria {} $ ".format(real,dolar))