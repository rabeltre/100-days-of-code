import  requests
from bs4 import  BeautifulSoup
HOST =  'https://pokemondb.net'
URL = '/pokedex/all'

def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup

def get_pokemon_species(url):
    soup = get_content(url)

    table = soup.find('table', class_='vitals-table')
    species = table.tbody.find_all('tr')[2].td.text

    return species


def show_pokemon_data():
    soup = get_content(HOST+URL)

    table = soup.find('table', {'id': 'pokedex'})

    for row in table.tbody.find_all('tr', limit=10):
        colums = row.find_all('td')

        name = colums[1].a.text
        type = [a.text for a in colums[2].find_all('a')]
        href = colums[1].a['href']

        next_url = HOST + href

        species = get_pokemon_species(next_url)

        print(name, *type, species, next_url)

if __name__=='__main__':
    show_pokemon_data()