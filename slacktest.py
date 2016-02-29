import time
from slackclient import SlackClient
import lunchbot_token #gitignored file

sc = SlackClient(lunchbot_token.lunchbot_token)

print sc.api_call("api.test")
print sc.api_call("channels.info", channel="C0DEN2FBL")
sc.api_call("chat.postMessage", channel="#general", text="Sssh. I am here to help...",
	username='Lunchbot', icon_emoji=':fork_and_knife:')
