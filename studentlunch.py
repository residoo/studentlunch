
## http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import bs4
import requests

res = requests.get('http://www.studentlunch.fi')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
##type(noStarchSoup)
allfoods = noStarchSoup.select(".food")

print allfoods[0].getText()

## Ersatt med requests?
""" import urllib
sock = urllib.urlopen("http://www.studentlunch.fi")
htmlSource = sock.read()
sock.close()
"""
## restaurang = raw_input("1. Arken\n2. Fanriken\n3. Gado\n4. Hanken\n5. Karen up\n6. Karen down\n>")

## anvand dictionaries for att halla koll pa namnen till restaurangerna
## restauranger = {1:"Arken", 2:"Fanriken", 3:"Gado", 4:"Hanken",5:"Karen up",6:"Karen down"}

## print htmlSource 



## hur losa problemet med skander?

## Hosting?





""" import requests

page = requests.get('http://www.studentlunch.fi')
"""