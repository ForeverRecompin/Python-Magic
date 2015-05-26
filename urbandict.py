from bs4 import BeautifulSoup as BS
from urllib.parse import urlencode
import requests,sys

def reveal():

    '''Finds the query result from the Urban Dict website.'''
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("What do you wanna look up? ")
        
    q = {"term":query}
    query = urlencode(q)
    base_url = "http://www.urbandictionary.com/define.php?"
    new_url = base_url + query
    print("URL:" + new_url + "\n" +"Meaning:")
    result = requests.get(new_url)
    resultSoup = BS(result.text)
    meaning = resultSoup.select('.meaning')
    
    if len(meaning) > 0:
        for each in meaning[:3]: #Top three results.
            print(each.getText())
    else:
        print("\n..Oops. What you looked up does not exist!")

if __name__ == "__main__":
    
    reveal()
