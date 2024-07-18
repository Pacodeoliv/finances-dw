#import
import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os 
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
data_filtered1hr = data3.loc['2024-07-17']
print("\n Dados Daily AAPL ")
print(data_filtered1hr)


data_filtered1hr.to_csv('dados_filtered.csv')