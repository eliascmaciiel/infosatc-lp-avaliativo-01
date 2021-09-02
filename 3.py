print("Olá, neste programa você poderá calcular quantas latas de tinta são necessárias para pintar uma parede.")

altura = float(input("Digite a altura da parede em metros."))
largura = float(input("Digite a largura da parede em metros."))

m2 = altura * largura

lata = m2 / 3.6

valor = lata * 107

print("Olá, para {}m², você irá precisar de {} latas de tinta, gastando um total de {} R$.".format(m2, lata, valor))