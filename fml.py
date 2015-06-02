from bs4 import BeautifulSoup as BS
import requests

def reveal():
    '''Gets a random FML quote from fmylife.com'''
    url = "http://www.fmylife.com/random"
    result = requests.get(url)
    resultSoup = BS(result.text)
    random_quote = resultSoup.find(attrs={'class': 'post article'})
    if len(random_quote) > 0:
        lol = random_quote.text
        print(lol[:lol.find("FML")+3]+"! xD")
    else:
        print("\n..Oops. Something went wrong. Please try again.")

if __name__ == "__main__":
    reveal()
