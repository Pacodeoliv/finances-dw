import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
import os
load_dotenv

alphaapikey = os.getenv('API_KEY')

if alphaapikey is True:
    print("Chave da API carregada")

if alphaapikey is None:
    raise ValueError("A chave da API não foi encontrada. Verifique se o arquivo está configurado corretamente")

