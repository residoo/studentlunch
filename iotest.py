# -*- coding: UTF-8 -*-

import bs4 # http://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests

# Print out all food for the day, without restaurant name
def output_food(food): 
	for x in range(len(food)): # For 0 to amount of entries in variable allfoods
		fooditem = food[x].getText()	# Put current food into string for checking
		if fooditem.endswith('*'):		# Check if fooditem has * at the end...
			print fooditem[:-1]			# ...and remove it if it does
		else:
			print fooditem


# Scrape the page!
webpage = requests.get('http://www.studentlunch.fi')
webpage.raise_for_status()
parsed_webpage = bs4.BeautifulSoup(webpage.text, "html.parser")

restaurants = parsed_webpage.select(".lunch-item") # Picks out all the restaurants

whatrestaurant = = raw_input("0. Arken\n1. Fanriken\n2. Gado\n3. Hanken\n4. Karen up\n5. Karen down\n>")

allfoods = restaurants[whatrestaurant].select(".food")

output_food(allfoods)
