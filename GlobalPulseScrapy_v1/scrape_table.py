import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import logging

with open('OutputLinks.json') as f:
    search_links = json.load(f)

unique_links = []

for i in range(len(search_links)):
    unique_links.append(search_links[i].get("link_url"))
    unique_links.append(search_links[i].get("parent_link"))

print(len(unique_links))
print(len(set(unique_links)))

urls = list(set(unique_links))

class HTMLTableParser:
    def __init__(self):
        pass

    def parse_url(self, url):
        if url:
            logging.info("parsing tables from", url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            return [(self.parse_html_table(hp, table = table)) for table in soup.find_all('table')]

    def parse_html_table(self, table):
        n_columns = 0
        n_rows = 0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        for row in table.find_all('tr'):

            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows+=1
                if n_columns < len(td_tags):
                    # Set the number of columns for our table
                    n_columns = len(td_tags)

        columns = range(0,n_columns)
        df = pd.DataFrame(columns = columns, index= range(0,n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            if row.find_all('th'):
                header_marker = 0
                headers = row.find_all('th')
                for header in headers:
                    df.iat[row_marker,header_marker] = header.get_text()
                    header_marker += 1
                row_marker += 1
            elif row.find_all('td'):
                column_marker = 0
                columns = row.find_all('td')
                for column in columns:
                    df.iat[row_marker,column_marker] = column.get_text()
                    column_marker += 1
                row_marker += 1

            # Convert to float if possible
        for col in df:
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass

        print("parsing complete")
        return df

hp = HTMLTableParser
url123 = "https://www.fastfoodmenuprices.com/arbys-prices/"

ph_table = hp.parse_url(hp, url = 'https://www.eia.gov/petroleum/gasdiesel/')
print(ph_table)
