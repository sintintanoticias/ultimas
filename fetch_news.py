import requests
import json
import os

# Your API key
API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'

# Define the endpoint for fetching news articles
URL = 'https://newsapi.org/v2/everything'

# Parameters for the API request
PARAMS = {
    'q': 'Nueva York',  # Keywords to search for
    'language': 'es',   # Language set to Spanish
    'sortBy': 'relevancy',  # Sort articles by relevancy
    'apiKey': API_KEY  # Your News API key
}

# Send a GET request to the News API
response = requests.get(URL, params=PARAMS)

# Convert the response to JSON
data = response.json()

# Check if the request was successful
if data['status'] == 'ok':
    # Get the articles from the response
    articles = data['articles']
    # Print the number of articles found
    print(f"Found {len(articles)} articles.")
    # Save the articles to a JSON file
    with open('news.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
else:
    # Print the error message if the request was not successful
    print(f"Error fetching news: {data['message']}")
