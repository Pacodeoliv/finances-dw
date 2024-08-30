import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os 
csv_file = 'dados_filtered29.csv'

# Verificando se o arquivo existe
csv_file = 'dados_filtered29.csv'

if os.path.exists(csv_file):
    # Carregar o CSV e imprimir as colunas para verificar o nome correto
    df = pd.read_csv(csv_file)
    
    # Exibir as colunas e as primeiras linhas para inspeção
    st.write("Colunas do DataFrame:", df.columns.tolist())
    st.write("Exibindo as primeiras linhas do DataFrame:")
    st.write(df.head())
    
    # Tentando identificar a coluna de data
    date_column = None
    for col in df.columns:
        if 'date' in col.lower() or 'timestamp' in col.lower():
            date_column = col
            break

    if date_column:
        # Convertemos a coluna de data para o formato datetime
        df[date_column] = pd.to_datetime(df[date_column])
        
        # Criando o gráfico de linhas
        fig = go.Figure()

        # Adicionando a linha 'open'
        if '1. open' in df.columns and '4. close' in df.columns:
            fig.add_trace(go.Scatter(
                x=df[date_column],
                y=df['1. open'],
                mode='lines',
                name='Open',
                line=dict(width=2, color='royalblue')
            ))

            # Adicionando a linha 'close'
            fig.add_trace(go.Scatter(
                x=df[date_column],
                y=df['4. close'],
                mode='lines',
                name='Close',
                line=dict(width=2, color='orange')
            ))

            # Atualizando o layout
            fig.update_layout(
                title='Gráfico de Linhas - Abertura e Fechamento da AAPL',
                xaxis_title='Horário',
                yaxis_title='Valor (USD)',
                showlegend=True
            )

            # Exibir no Streamlit
            st.title("Gráfico de Linhas - AAPL")
            st.plotly_chart(fig)
        else:
            st.error("As colunas 'open' e 'close' não foram encontradas no CSV.")
    else:
        st.error("Nenhuma coluna correspondente a data/timestamp foi encontrada.")
else:
    st.error("Arquivo CSV não encontrado. Verifique o caminho e a existência do arquivo.")
