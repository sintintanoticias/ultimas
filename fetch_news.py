import requests
import json

API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'
COUNTRY = 'do'  # Dominican Republic
LANGUAGE = 'es'  # Spanish

def fetch_news():
    try:
        url = f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&language={LANGUAGE}&apiKey={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        if news_data['status'] == 'ok' and news_data['totalResults'] > 0:
            # Save the news data to a JSON file
            with open('news.json', 'w', encoding='utf-8') as json_file:
                json.dump(news_data, json_file, ensure_ascii=False, indent=4)
            print("News data fetched successfully.")
        else:
            print("No articles found. Check the query parameters.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")

if __name__ == '__main__':
    fetch_news()
