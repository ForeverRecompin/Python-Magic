from bs4 import BeautifulSoup as BS
from urllib.parse import urlencode
import requests,sys

def reveal():

    '''Finds the query weather result from the wunderground website.'''
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("What do you wanna look up? (Format: City, State, Country) ")
        
    q = {"query":query}
    query = urlencode(q)
    base_url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?"
    new_url = base_url + query
    print("URL:" + new_url + "\n" +"Current Weather Forecast for %s:" %query)
    result = requests.get(new_url)
    resultSoup = BS(result.text)
    currentTemp = resultSoup.find(id="curTemp")
    
    if currentTemp and len(currentTemp) > 0:
            print(currentTemp.span.get_text().strip().replace("\n", " "))
            print("Clouds/Sky: "+resultSoup.find(id="cc1").find(id="curCond").span.get_text())
    else:
        print("\n..Oops. Something went wrong.") 

if __name__ == "__main__":
    
    reveal()
