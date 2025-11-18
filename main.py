from src.Sistema import Sistema

# URL da API JSearch
api = "https://jsearch.p.rapidapi.com/search"

# Headers da api com a chave
headers = {
    "x-rapidapi-host": "jsearch.p.rapidapi.com",
    "x-rapidapi-key": "3198d88c8emshe3e90e0fabaab5ep12b653jsn46165634ee1a"
}

# Instanciando a classe sistema passando headers e a api
sistema = Sistema(headers=headers, api=api)

# Loop principal que roda o menu do sistema
while True:
    sistema.menu()