import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os
load_dotenv


# Projeto 1, coletar dados da api que me trás coisas da bolsa de valores e salvar em csv. (Quero aprender como fazer request em API e como escrever arquivos)

alphaapikey = os.getenv('API_KEY')

if alphaapikey is True:
    print("Chave da API carregada")

if alphaapikey is None:
    raise ValueError("A chave da API não foi encontrada. Verifique se o arquivo está configurado corretamente")

