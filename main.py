from src.Sistema import Sistema

api = "https://jsearch.p.rapidapi.com/search"
headers = {
    "x-rapidapi-key": "3198d88c8emshe3e90e0fabaab5ep12b653jsn46165634ee1a",
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

sistema = Sistema(headers=headers, api=api)

while True:
    sistema.menu()