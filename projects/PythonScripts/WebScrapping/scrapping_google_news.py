import requests
from bs4 import BeautifulSoup
from datetime import  datetime

URL='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'

if __name__== '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        #news_dia_mes_año.txt
        now = datetime.now().strftime('%d_%m_%Y')
        file_path = f'news/news_{now}.txt'

        with open(file_path, '+w') as file:
            i = 0
            for h3 in soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb'):
                title = h3.a.text
                href = h3.a['href']
                i+=1
                file.write(str(i) + " " + title + " --> " + href + '\n')
