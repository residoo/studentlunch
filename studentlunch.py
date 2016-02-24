
## Ersätt med requests?
import urllib
sock = urllib.urlopen("http://www.studentlunch.fi")
htmlSource = sock.read()
sock.close()

restaurang = raw_input("1. Arken\n2. Fanriken\n3.Gado\n4. Hanken\n5. Karen up\n6. Karen down\n>")



## print htmlSource 


## använd dictionaries för att hålla koll på namnen till restaurangerna
## hur lösa problemet med skander?

## Hosting?

## behöver Beautiful Soup modul




""" import requests

page = requests.get('http://www.studentlunch.fi')
"""