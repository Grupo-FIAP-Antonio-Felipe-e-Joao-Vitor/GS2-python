from src.calcular_taxa_crescimento_individual import calcular_taxa_crescimento_individual

def calcular_taxa_crescimento (url, headers, lista, soma = 0):
    if not lista:
        return soma

    profissao = lista[0]
    taxa = calcular_taxa_crescimento_individual(url, headers, profissao)

    return calcular_taxa_crescimento(url, headers, lista[1:], soma + taxa)