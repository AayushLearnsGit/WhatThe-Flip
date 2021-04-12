import bs4
import requests
import time

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}

class checkfor_this():

    def __init__(self, url= "https://www.flipkart.com/"):
        self.url = url
        self.title, self.last_price = self._check()

    def _check(self):
        content = requests.request('GET', url= self.url, headers= headers) 
        content.raise_for_status()
        soup = bs4.BeautifulSoup(content.content, features="lxml")
        try:
          price = int(soup.find("div", attrs= "_30jeq3 _16Jk6d").text[1:].strip().replace(",", ''))
          title = soup.find("span", attrs= "B_NuCI").text
          return title, price
        except:
          print('''Got an error - try fixing by:\n• Checking the URL\n• Connect me! Scraping doesn't work always!''')