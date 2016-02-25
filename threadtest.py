# threadtest.py
# -*- coding: UTF-8 -*-

import threading
import time
from slackclient import SlackClient
import slacktoken #gitignored file

# Get access to Slack.
sc = SlackClient(slacktoken.slacktoken)

	
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        listen_to_Slack(self.name, self.counter, 5)
        print "Exiting " + self.name

def listen_to_Slack(threadName, delay, counter):
	if sc.rtm_connect():
		while counter:
			if exitFlag:
				threadName.exit()
			time.sleep(delay)
			print "Listening... %s: %s" % (threadName, time.ctime(time.time()))
			print sc.rtm_read()
			counter -= 1
	else:
		print "Connection Failed, invalid token?"
		
		
		
		
# Create new threads
thread1 = myThread(1, "Thread-1", 1)

# Start new Threads
thread1.start()


print "Exiting Main Thread"