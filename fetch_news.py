import requests
import json

def fetch_news():
    api_key = '7005a6609b9a4b0a8c3a0e35124817d4'  # Replace with your API key
    url = f'https://newsapi.org/v2/top-headlines?country=do&language=es&apiKey={api_key}'

    response = requests.get(url)
    news_data = response.json()

    # Save the news data to a JSON file
    with open('news.json', 'w', encoding='utf-8') as json_file:
        json.dump(news_data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    fetch_news()
