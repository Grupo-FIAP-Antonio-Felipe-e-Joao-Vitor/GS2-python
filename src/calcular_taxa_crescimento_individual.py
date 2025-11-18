from src.obter_tendencias_emprego import obter_tendencias_emprego

def calcular_taxa_crescimento_individual (url, headers, profissao):

    antigas = obter_tendencias_emprego(url, headers, profissao, 10, "br", "month")   # Pega as vagas de emprego do último mês
    recentes = obter_tendencias_emprego(url, headers, profissao, 10, "br", "all")  # Pega as vagas de emprego dos últimos tempos

    quantidade_antigas = len(antigas)   # Pega quantas vagas tivemos há um mês
    quantidade_recentes = len(recentes) # Pega quantas vagas tivemos há três dias

    try:
        # Calcula a taxa de crescimento
        taxa = (quantidade_recentes - quantidade_antigas)/(quantidade_recentes + quantidade_antigas) * 100 

        # Retorna a taxa calculada
        return taxa
    
    # Trata erro de divisão por 0
    except ZeroDivisionError:

        # Retorna 0 se a divisão tiver 0 no denominador
        return 0