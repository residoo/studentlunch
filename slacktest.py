import time
from slackclient import SlackClient

# found at https://api.slack.com/web#authentication
token = "xoxp-13493019173-13497086977-22933513152-310fde5159"      
sc = SlackClient(token)

print sc.api_call("api.test")
print sc.api_call("channels.info", channel="C0DEN2FBL")
print sc.api_call(
    "chat.postMessage", channel="#bitter-white-men", text="Pythontest :milli:",
    username='Lunchbot', icon_emoji=':robot_face:'
)