from src.calcular_taxa_crescimento_individual import calcular_taxa_crescimento_individual

def calcular_taxa_crescimento (url, headers, lista, soma = 0):

    # Condição de parada
    if not lista:
        return soma

    # Pega o primeiro item da lista e calcula a taxa
    profissao = lista[0]
    taxa = calcular_taxa_crescimento_individual(url, headers, profissao)

    # Chama a função de novo, passando uma nova lista que não possui o primeiro elemento da outra lista e passa
    # a soma + taxa
    return calcular_taxa_crescimento(url, headers, lista[1:], soma + taxa)