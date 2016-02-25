import time
from slackclient import SlackClient
import slacktoken #gitignored file

sc = SlackClient(slacktoken.slacktoken)

if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"