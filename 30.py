print("Olá, seja muito bem vindo, nesse programa iremos calcular quantos dólares você teria.")

real = float(input("Digite um valor em R$: "))

cotacao = float(input("Digite a cotação atual do Dolar: "))

dolar = real / cotacao

print("No caso da cotação ser {}, você com {} R$ teria {} $ ".format(cotacao,real,dolar))