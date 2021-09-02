premio = float(input("Digite o valor que você ganhou na loteria."))

valorimposto = premio * 0.07

imposto = premio - valorimposto

calculo1 = imposto * 0.46

calculo2 = imposto * 0.32

calculo3 = imposto * 0.22

print("Novamente parabéns! O valor total do prêmio foi de: {} R$".format(premio))

print ("O dinheiro que você perdeu para o estado por impostos foi: {:.3} R$".format(valorimposto))

print ("O primeiro ganhador ganhará: {} R$".format(calculo1))

print ("O segundo ganhador ganhará: {} R$".format(calculo2))

print ("O terceiro ganhador ganhará: {} R$".format(calculo3))

