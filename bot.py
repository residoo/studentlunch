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

sc = SlackClient(lunchbot_token.lunchbot_token)
print ("SlackClient ready to go...")

counter = 10

print ("Initializations DONE")

# METHODS

def bot_talk(channel, message):
	sc.api_call("chat.postMessage", channel=channel, text=message,
	username='Lunchbot', icon_emoji=':fork_and_knife:')

def listen_to_message(evt):
	#bot_talk(evt["channel"],"I heard something")
	#bot_talk(evt["channel"],"It was " + evt["user"])
	if evt["text"] == unicode("lunchbot gado"):
		bot_talk(evt["channel"],"I heard something")
	if unicode("lunchbot") in evt["text"]:
		bot_talk(evt["channel"],"I definitely heard something")

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