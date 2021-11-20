
import requests
from bs4 import BeautifulSoup
import openpyxl


url_pagina = 'https://www.leagueofgraphs.com/es/rankings/summoners/euw'

dicc_players = {
    'ranking': '',
    'name': '',
    'elo': '',
    'victorias': '',
    'winrate': '',
}

def cargar_pagina():
    html = requests.get('https://www.leagueofgraphs.com/es/rankings/summoners/euw').content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def elementos_ranking(soup):
    tabla_list = list()
    lista_ranking = soup.findAll('table', {'class': 'data_table summonerRankingsTable with_sortable_column'})

    for elemento in lista_ranking:
        ranking = elemento.find('td', {'class':'text-right hide-for-small-down'})

    return tabla_list

def cargar_todas_paginas():
    soup_list = list()
    for num_pag in range(1, 2):
        soup = cargar_pagina(url_pagina + str(num_pag))
        soup_list.append(soup)
    return soup_list

cargar_todas_paginas()