import requests
import json

API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'  # Your NewsAPI key

def fetch_news():
    try:
        # Fetch top headlines from the US
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        # Save the news data to a JSON file
        with open('news.json', 'w', encoding='utf-8') as json_file:
            json.dump(news_data, json_file, ensure_ascii=False, indent=4)
        print("News data fetched successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")

if __name__ == '__main__':
    fetch_news()
