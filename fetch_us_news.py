import requests
import json

# Clave API para News API
API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'

# URL del endpoint
URL = 'https://newsapi.org/v2/everything'

# Parámetros para la solicitud
PARAMS = {
    'q': 'República Dominicana',  # Palabra clave para República Dominicana
    'language': 'es',             # Idioma establecido en español
    'sortBy': 'relevancy',        # Ordenar resultados por relevancia
    'apiKey': API_KEY             # Clave API
}

# Realizar la solicitud GET a la API de NewsAPI
response = requests.get(URL, params=PARAMS)

# Convertir la respuesta a JSON
data = response.json()

# Verificar si la solicitud fue exitosa
if data['status'] == 'ok' and data['totalResults'] > 0:
    # Extraer artículos de la respuesta
    articles = data['articles']
    # Guardar los artículos en un archivo JSON
    with open('news.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
else:
    # Imprimir mensaje de error si hay alguno
    print(f"Error fetching news: {data.get('message', 'No articles found')}")
