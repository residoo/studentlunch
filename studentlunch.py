
## http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import bs4
import requests

webpage = requests.get('http://www.studentlunch.fi')
webpage.raise_for_status()
parsed_webpage = bs4.BeautifulSoup(webpage.text, "html.parser")
##type(parsed_webpage)

# restaurants = parsed_webpage.select(".lunch-item") # Picks out all the restaurants
# print restaurants[0].getText()
# arkenfood = restaurants[0].select(".food")

"""
for x in range(len(restaurants)):
	print restaurants[x]
"""

food = parsed_webpage.select(".lunch-item-food .food")
foodprint = food[1].getText()
print foodprint.encode('utf-8')

"""
# for x in range(len(parsed_webpage.select("lunch-item"))):
for x in range(6):
	food[x] = parsed_webpage.select("lunch-item:nth-of-type(x) .food")
	print x
"""
	
"""	
for x in range(len(food[0])): # For 0 to amount of entries in variable allfoods
	
	fooditem = food[x].getText()	# Put current food into string for checking
	
	if fooditem.endswith('*'):		# Check if fooditem has * at the end...
		print fooditem[:-1]			# ...and remove it if it does
	else:
		print fooditem
"""
		
		
"""
allfoods = parsed_webpage.select(".food")

# Print out all food, without restaurant name
for x in range(len(allfoods)): # For 0 to amount of entries in variable allfoods
	
	fooditem = allfoods[x].getText()	# Put current food into string for checking
	
	if fooditem.endswith('*'):		# Check if fooditem has * at the end...
		print fooditem[:-1]			# ...and remove it if it does
	else:
		print fooditem
"""
# print allfoods[0].getText()

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

""" Dictionary med restauranger som keys som pekar pa matlistorna?

lunch = {"Arken":[],"Fanriken":[],"Gado",[],"Hanken":[],"Karen up":[],"Karen down":[]}
"""


""" import requests

page = requests.get('http://www.studentlunch.fi')
"""