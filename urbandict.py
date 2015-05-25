from bs4 import BeautifulSoup as BS
import requests,webbrowser,sys

'''
if len(sys.argv) > 1:
    key = " ".join(sys.argv[1:])
    key = key.replace(" ","+")
else:
    key = " "
    raise ValueError("You provided me with nothing!")
'''

key = str(input("What do you wanna look up? "))

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
        if count == 3: #Currently shows top three results. Tweak this if need be.
            break
else:
    print("\n..Oops. What you looked up ain't does not exist!")
