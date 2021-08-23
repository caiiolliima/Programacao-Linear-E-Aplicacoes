def somaImposto(taxaImposto, custo):
    return custo + (custo * taxaImposto / 100)

preço = float(input('Informe o valor do produto: R$ '))
taxa = float(input("Informe a taxa de juros: "))

total = somaImposto(taxa, preço)
print("O valor final do produto com juros é R${:.2f}".format(total))
