import requests

def obter_tendencias_emprego(url, headers, palavra_chave = "IA"):
    """
    Faz uma requisição à API JSearch e retorna uma lista de profissões em alta.
    """
    

    querystring = {
        "query": palavra_chave,   # palavra-chave de busca
        "page": "1",
        "num_pages": "1",
        "country": "br",
        "date_posted": "all"
    }

    try:
        # Faz a requisição
        response = requests.get(url, headers=headers, params=querystring)

        # Verifica se houve erro HTTP (ex: 401, 404, 500)
        response.raise_for_status()

        # Converte para JSON
        data = response.json()

        # Verifica se a resposta tem a chave 'data'
        if "data" not in data:
            print("Resposta inesperada da API:", data)
            return []

        # Monta a lista de profissões (máximo 10)
        profissoes = []
        for item in data["data"][:10]:
            profissao = {
                "titulo": item.get("job_title"),
                "empresa": item.get("employer_name"),
                "local": item.get("job_location"),
                "tipo": item.get("job_employment_type"),
                "publicado": item.get("job_posted_at"),
                "link": item.get("job_apply_link")
            }
            profissoes.append(profissao)

        return profissoes

    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro na requisição:", err)
    except Exception as e:
        print("Erro geral:", e)
