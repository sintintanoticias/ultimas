import requests
import json

# API key for News API
API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'

# Define the endpoint URL for US top headlines
URL = 'https://newsapi.org/v2/top-headlines'

# Parameters for the request
PARAMS = {
    'country': 'us',             # Country code for the United States
    'language': 'es',            # Language set to Spanish
    'sortBy': 'relevancy',       # Sort results by relevancy
    'apiKey': API_KEY            # API Key
}

# Make the GET request to News API
response = requests.get(URL, params=PARAMS)

# Convert the response to JSON
data = response.json()

# Check if the request was successful
if data['status'] == 'ok' and data['totalResults'] > 0:
    # Extract articles from the response
    articles = data['articles']
    # Print the number of articles found
    print(f"Found {len(articles)} articles.")
    # Save the articles to a JSON file
    with open('us_top_headlines.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
else:
    # Print the error message if any
    print(f"Error fetching news: {data.get('message', 'No articles found')}")
