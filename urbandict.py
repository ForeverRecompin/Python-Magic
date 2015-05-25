from bs4 import BeautifulSoup as BS
import requests,sys

def reveal(query):

    '''Finds the query result from the Urban Dict website.'''
    
    ''' Tweak this if you want to use the script from the command line.

    if len(sys.argv) > 1:
        key = " ".join(sys.argv[1:])
        key = key.replace(" ","+")
    else:
        key = " "
        raise ValueError("You provided me with nothing!")
    '''

    base_url = "http://www.urbandictionary.com/define.php?term="
    new_url = base_url + key

    result = requests.get(new_url)
    resultSoup = BS(result.text)
    meaning = resultSoup.select('.meaning')

    count = 0
    if len(meaning) > 0:
        for each in meaning:
            print(each.getText())
            count += 1
            if count == 3: #Currently shows top three results. Change this if you have to.
                break
    else:
        print("\n..Oops. What you looked up does not exist!")

if __name__ == "__main__":
    
    key = str(input("What do you wanna look up? "))
    reveal(key)
