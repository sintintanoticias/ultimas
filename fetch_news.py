import requests

def fetch_news(query, language, sort_by='publishedAt'):
    api_key = 'your_api_key_here'
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'language': language,
        'sortBy': sort_by,
        'apiKey': api_key
    }
    
    response = requests.get(url, params=params)
    return response.json()

def fetch_combined_news():
    news_sets = []
    
    # Fetch US top headlines in Spanish
    us_headlines_spanish = fetch_news('Estados Unidos', 'es')
    news_sets.append(us_headlines_spanish)
    
    # Fetch Dominican Republic news
    dominican_republic_news = fetch_news('República Dominicana', 'es')
    news_sets.append(dominican_republic_news)
    
    # Fetch another topic, e.g., technology in Spanish
    technology_news = fetch_news('tecnología', 'es')
    news_sets.append(technology_news)

    # Combine all articles
    combined_articles = []
    for news_set in news_sets:
        if news_set['status'] == 'ok':
            combined_articles.extend(news_set['articles'])

    return combined_articles

def main():
    articles = fetch_combined_news()
    
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published at: {article['publishedAt']}")
        print(f"URL: {article['url']}")
        print('-' * 40)

if __name__ == "__main__":
    main()
