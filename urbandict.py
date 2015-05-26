from bs4 import BeautifulSoup as BS
import requests,sys

def reveal():

    '''Finds the query result from the Urban Dict website.'''
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        query = query.replace(" ","+")
    else:
        query = str(input("What do you wanna look up? "))
    
    base_url = "http://www.urbandictionary.com/define.php?term="
    new_url = base_url + query

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
