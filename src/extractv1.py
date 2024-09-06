import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os
load_dotenv()


# Projeto 1, coletar dados da api que me trás coisas da bolsa de valores e salvar em csv. (Quero aprender como fazer request em API e como escrever arquivos)

alphaapikey = os.getenv('API_KEY')

if alphaapikey :
    print("Chave da API carregada")
else:
    raise ValueError("A chave da API não foi encontrada. Verifique se o arquivo está configurado corretamente")


# Define qual key usar, formato de saida doque requisitar no TS
ts = TimeSeries(key=alphaapikey, output_format='pandas')

# Realizar a busca pelo simbolo entre 'XXXX'
dataBBAS, meta_dataBBAS = ts.get_symbol_search('banco do brasil')

def dadosBBAS():
     if dataBBAS.empty:
        print("Nenhum dado foi retornado.")
     else:  
        print("Dados:")
        print(dataBBAS)
        print("\nMeta Dados (Dados sobre dados):")
        print(meta_dataBBAS)

        return dadosBBAS