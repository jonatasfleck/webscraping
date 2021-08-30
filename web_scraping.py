
# 2 PARSEAR O CONTEUDO HTML - BEAUTIFULSOUP
# 3 ESTRUTURAR CONTEÚDO EM UM DATA FRAME - PANDAS 
# 4 TRANSFORMAR OS DADOS EM UM DICIONARIO DE DADOS PRÓPRIO 
# 5 CONVERTER E SALVAR O ARQUIVO JSON





import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1 PEGAR O CONTEUDO HTML - BEAUTIFULSOUP
url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)

driver.quit()
