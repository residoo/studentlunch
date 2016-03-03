# bot.py
# -*- coding: UTF-8 -*-

# IMPORTS
print ("Starting imports...  "),

import time
import json, yaml, re, bs4, requests
from slackclient import SlackClient
import lunchbot_token #gitignored file

print ("DONE")

# INITIALIZATIONS
print ("Starting inits...")

# Scrape the page!
webpage = requests.get('http://www.studentlunch.fi')
webpage.raise_for_status()
parsed_webpage = bs4.BeautifulSoup(webpage.text, "html.parser")
print ("Webpage OK...  "),

restaurants = parsed_webpage.select(".lunch-item") # Picks out all the restaurants
print ("Restaurants OK...  "),

sc = SlackClient(lunchbot_token.lunchbot_token)
print ("SlackClient ready to go...")

counter = 60
all_restaurants = {"arken" : 0, "fänriken" : 1, "gado" : 2, "hanken" : 3, "karen up" : 4, "karen down" : 5}

print ("Initializations DONE")

# METHODS

def bot_talk(channel, message):
	sc.api_call("chat.postMessage", channel=channel, text=message,
	username='Lunchbot', icon_emoji=':fork_and_knife:')
	
# Print out all food for the day, without restaurant name
def output_food(food, evt): 
	for x in range(len(food)): 			# For 0 to amount of entries
		fooditem = food[x].getText()	# Put current food into string for checking
		if fooditem.endswith('*'):		# Check if fooditem has * at the end...
			bot_talk(evt["channel"],fooditem[:-1])			# ...and remove it if it does
		else:
			bot_talk(evt["channel"],fooditem)			# ...and if not just print it as is

def listen_to_message(evt):
	#bot_talk(evt["channel"],"I heard something")
	#bot_talk(evt["channel"],"It was " + evt["user"])
	"""
	if unicode("lunchbot") in evt["text"]:
		bot_talk(evt["channel"],"I heard something")
	if evt["text"] == unicode("lunchbot gado"):
		bot_talk(evt["channel"],"I definitely heard something")
	"""
	message = evt["text"].encode('ascii', 'replace') 	# Convering to string datatype that I can deal with
	message = message.lower() 							# make it all lower case
	if "lunchbot" in message:							# Must we bother...?
		print "Ok, we might need to deal with this"
		words = message.split()							
		if words[0] == "lunchbot" and len(words) == 2:	# Len might go up to 3, but for testing						
			if words[1] in all_restaurants:
				print "found the restaurant, it's " + words[1]
				restaurant = words[1]
				print restaurant
				print all_restaurants[restaurant]
				allfoods = restaurants[all_restaurants[restaurant]].select(".food")
				output_food(allfoods, evt)
	
if sc.rtm_connect():
	print 
	print "Bot is listening."
	print 
	
	print "Checking for users"
	users = str(sc.api_call("users.list"))
	#print users
	if unicode('members') in users:
		print "Found users!"
		print
	
	if unicode('name') in users:
		print "Found names!"
		print users.find(unicode('name'))
	

	
	"""
	sc.api_call("chat.postMessage", channel="D0PEE8ABV", text="Listening...",
	username='Lunchbot', icon_emoji=':fork_and_knife:')
	"""
	
	bot_talk("D0PEE8ABV", "åäö")
	
	while counter > 0:
		counter -= 1
		events = sc.rtm_read()
		for evt in events:
			if "type" in evt:
				print "Event logged: " + evt["type"]
				#m = unicode('message')
				if evt["type"] == unicode('message') and "text" in evt:
					# print evt["text"]
					if "username" in evt and evt["username"] == "Lunchbot":
						print "Lunchbot speaketh!"
					else:
						listen_to_message(evt)
		
		time.sleep(1)
		
		
else:
    print "Connection Failed, invalid token?"

print	
print "End of Run"