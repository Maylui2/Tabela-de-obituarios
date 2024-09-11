from prettytable import PrettyTable
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://omunicipiojoinville.com/obituario-de-joinville-2808-a-0609/'   #link do obituario da minha cidade
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = pd.read_html(str(soup))

    if tables:
        for i, table in enumerate(tables):
            print(f"Table {i}:")
            
            # Cria uma tabela PrettyTable
            pretty_table = PrettyTable()
            pretty_table.field_names = table.columns
            
            # Adiciona linhas à tabela PrettyTable
            for row in table.itertuples(index=False):
                pretty_table.add_row(row)
            
            # Imprime a tabela formatada
            print(pretty_table)
            print("\n")
    else:
        print("No tables found.")
else:
    print(f'Failed to retrieve the page: {response.status_code}')
