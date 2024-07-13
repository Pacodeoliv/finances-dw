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
data, meta_data = ts.get_symbol_search('itau')

# Salvando em arquivo csv
#data.to_csv('dados_itau.csv')


print("Dados:")
print(data)

print("\nMetadados:")
print(meta_data)
