import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os 
csv_file = 'dados_filtered29.csv'

# Carregar os dados do CSV gerado
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    st.write("Colunas do Dataframe:", df.columns)

    # Verfique se o nome da coluna de data está correto
    # Vamos listar todas as colunas para garantir que estamos acessando a coluna correta
    st.write("Exibindo as primeiras linhas do Dataframe")
    st.write(df.head())

    # Certifique-se de que o nome da coluna está coreto (ajuste conforme necessário)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['timestamp'])
    elif 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(['timestamp'])
        df.rename(columns={'timestamp': 'date'}, inplace=True)

    # Criando o gráfico
    fig = go.Figure()

    # Verificando se as colunas 'open' e 'close' estão corretas também
    if '1. open' in df.columns and '4. close' in df.columns:
        
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['1. open'],
            mode='lines',
            name='Open',
            stackgroup= "one", # Define as áreas empilhadas
            line=dict(width= 0.5, color='royalblue')
        ))

        # Adicionando a série 'close'
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['4. close'],
            mode='lines',
            name='Close',
            stackgroup='one', # Define as áreas empilhadas
            line=dict(width= 0.5, color='royalblue')
        ))

        # Atualizando o layout
        fig.update_layout(
            title='Gráfico de Áreas Empilhadas - Abertura e Fechamento da AAPL',
            xaxis_title='Horário',
            yaxis_title='Valor(USD)',
            showlegend=True
        )

        # Exibir no Streamlit
        st.title("Gráfico de Áreas Empilhadas - AAPL - 29 de Agosto")
        st.plotly_chart(fig)
    else:
        st.error("As colunas 'Open' e 'close' não foram encontradas no CSV")
else:
    st.error("Arquivo CSV não encontrado. Verifique o caminho e a existência do arquivo.")
