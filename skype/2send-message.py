from skpy import Skype
def post_message(msg,channel_id): 
  "Post a message" 
  sk = Skype("<email>","<password>")
  channel = sk.chats.chat("19:75a59852398*****************7aad872586@thread.skype") 
  channel.sendMsg(msg)
  print("Message Sent")

post_message("Good Morning!!","channel-id@thread.skype")

