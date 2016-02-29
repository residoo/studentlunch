# lunchbot_test.py
# -*- coding: UTF-8 -*-

import time
import json, yaml, re
from slackclient import SlackClient
import lunchbot_token #gitignored file

sc = SlackClient(lunchbot_token.lunchbot_token)

counter = 10
# event = {}


if sc.rtm_connect():
	print "Listening..."
	sc.api_call("chat.postMessage", channel="D0PEE8ABV", text="Listening...",
	username='Lunchbot', icon_emoji=':fork_and_knife:')
	while counter > 0:
		counter -= 1
		# print sc.rtm_read()
		events = sc.rtm_read()
		#print "After load"
		#print events
		#print "After json"
		#parsed_events = json.loads(events)
		#print "Go into loop"
		#print type(event)
		for evt in events:
			#print evt
			if "type" in evt:
				print evt["type"]
				#print "Found type!"
				#print type(evt["type"])
				m = unicode('message')
				if evt["type"] == m and "text" in evt:
					print evt["text"]
		
		# print len(event)
		# if event["type"] == "message":
			# print "message received!"
		#for i in event:
			# print i
		time.sleep(1)
		
		
else:
    print "Connection Failed, invalid token?"
	
print "End of Run"