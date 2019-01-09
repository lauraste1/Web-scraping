import requests
from bs4 import BeautifulSoup

url = 'https://www.abc.net.au/'
web_page = requests.get(url)
web_page.encoding = 'UTF-8'
soup = BeautifulSoup(web_page.text, 'html.parser')
top_news = soup.find("div", {"id": "hero"})

articlelinks = []
for article in top_news.find_all('a')[0:]:
    articlelinks.append(article.get('href'))

for a in articlelinks:
    url1 = f"{a}"
    req = requests.get(url1)
    req.encoding = 'UTF-8'
    newsoup = BeautifulSoup(req.text, 'html.parser')

    title = newsoup.find('h1').text
    by = newsoup.find('div', attrs={'class':'byline'})
    date = newsoup.find('span', attrs={"class":"timestamp"}).text
    f_date = date.strip()
    para = newsoup.find_all("p")[1].text

    print(title)
    if by:
        byline = newsoup.find('div', attrs={'class':'byline'}).text
        f_byline=byline.strip()
        print(f_byline)
    print(f_date)
    print(para)
    print("\n")
