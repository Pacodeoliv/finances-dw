#import
import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os 
import plotly.graph_objects as go
import plotly.io as pio
load_dotenv()

AV_API_KEY = os.getenv('API_KEY')
if AV_API_KEY is None:
    raise ValueError("A chave da API não foi encontrada no arquivo .env. Verifique se o arquivo está configurado corretamente.")

print("Chave da API carregada:", AV_API_KEY)

ts = TimeSeries(key=AV_API_KEY, output_format='pandas')

# Realizando a busca pelo símbolo 'itau'
data, meta_data = ts.get_symbol_search('apple')

dataitau, meta_dataitau = ts.get_symbol_search('itau')



# Salvando em arquivo csv
#data.to_csv('dados_extract.csv')

"""
print("Dados:")
print(data)

print("\nMetadados:")
print(meta_data)

print("\nDados:")
print(dataitau)

print("\nMetadados:")
print(meta_dataitau)

"""
data3,meta_data3 = ts.get_intraday(symbol= 'AAPL',interval= '60min', outputsize= 'full')
data_filtered1hr = data3.loc['2024-08-29']
print("\n Dados Daily AAPL ")
print(data_filtered1hr)


data_filtered1hr.to_csv('dados_filtered29.csv')


# Configure o renderizador (notebook ou browser, conforme necessário)
pio.renderers.default = 'browser'

# Seus dados em um DataFrame
data = {
    'date': ['2024-08-29 19:00:00', '2024-08-29 18:00:00', '2024-08-29 17:00:00', '2024-08-29 16:00:00'],
    'open': [230.05, 230.26, 230.21, 229.83],
    'close': [230.29, 230.00, 230.31, 230.259]
}

df = pd.DataFrame(data)

# Convertendo o campo 'date' para datetime
df['date'] = pd.to_datetime(df['date'])

# Criando o gráfico
fig = go.Figure()

# Adicionando a série 'open'
fig.add_trace(go.Bar(
    x=df['open'],
    y=df['date'],
    orientation='h',
    name='Open',
    marker=dict(color='royalblue')
))

# Adicionando a série 'close'
fig.add_trace(go.Bar(
    x=df['close'],
    y=df['date'],
    orientation='h',
    name='Close',
    marker=dict(color='orange')
))

# Atualizando o layout
fig.update_layout(
    title='Abertura e Fechamento da AAPL ao Longo do Tempo',
    xaxis_title='Valor (USD)',
    yaxis_title='Horário',
    barmode='group'
)

# Exibindo o gráfico
fig.show()