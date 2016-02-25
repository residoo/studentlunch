import time
from slackclient import SlackClient
import slacktoken #gitignored file

sc = SlackClient(slacktoken.slacktoken)

print sc.api_call("api.test")
print sc.api_call("channels.info", channel="C0DEN2FBL")
print sc.api_call(
    "chat.postMessage", channel="@dallester", text="Pythontest :milli:",
    username='Lunchbot', icon_emoji=':robot_face:'
)