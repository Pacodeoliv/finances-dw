import pandas as pd 
import yfinance as yf
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()


# Ticker da BYD ADR nos EUA
byd_adr = yf.Ticker("BYDDY")
# Obter informações gerais da empresa
info_byd = byd_adr.info
# print(info_byd)


byd_historico = byd_adr.history()
#print(byd_historico)
byd_historico.to_csv('bydhistorico.csv')
