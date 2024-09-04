import requests
import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


# Definir sua chave de API e endpoint da Alpha Vantage
API_KEY = os.getenv('API_KEY')
NEWS_ENDPOINT = 'https://www.alphavantage.co/query'

# Função para obter notícias da API
def get_news_data(tickers=None, topics=None, time_from=None, time_to=None, limit=50):
    params = {
        'function': 'NEWS_SENTIMENT',
        'apikey': API_KEY,
        'limit': limit
    }
    if tickers:
        params['tickers'] = tickers
    if topics:
        params['topics'] = topics
    if time_from:
        params['time_from'] = time_from
    if time_to:
        params['time_to'] = time_to

    response = requests.get(NEWS_ENDPOINT, params=params)
    

    # Exibir os parâmetros da solicitação 13:02 04SEP
    st.write("Parâmetros da solicitação:", params)

    response = requests.get(NEWS_ENDPOINT, params=params)
    
    # Exibir a resposta bruta da API 13:02 04SEP
    st.write("Resposta da API:", response.json())

    return response.json()


# Função para processar o JSON da API
def process_news_data(news_data):
    articles = news_data.get('feed', [])
    processed_data = []

    for article in articles:
        processed_data.append({
            'title': article['title'],
            'sentiment': article['overall_sentiment_score'],
            'date': article['time_published'],
            'source': article['source'],
            'url': article['url']
        })

    return pd.DataFrame(processed_data)



# Função principal
def main():
    st.title("Market News & Sentiment Dashboard")
    
    # Inputs do usuário
    tickers = st.text_input("Digite os tickers (ex: AAPL, TSLA, CRYPTO:BTC)", value="")
    topics = st.text_input("Digite os tópicos (ex: technology, earnings)", value="technology")
    time_from = st.text_input("Data inicial (YYYYMMDDTHHMM)", value="20240101T0000")
    time_to = st.text_input("Data final (YYYYMMDDTHHMM)", value=datetime.now().strftime("%Y%m%dT%H%M"))

    # Botão para buscar dados
    if st.button("Buscar Dados"):
        news_data = get_news_data(tickers=tickers, topics=topics, time_from=time_from, time_to=time_to)
        if 'feed' in news_data:
            df = process_news_data(news_data)
            st.write(df)
           # plot_sentiment(df)
        else:
            st.error("Nenhum dado encontrado ou erro na API")

# Executar o app com Streamlit
if __name__ == "__main__":
    main()