##First file will provide the laste group chat id

```
from skpy import Skype
email = "<email>"
password = "<password>"
sk = Skype("<email>","<password>")
channel = sk.chats.recent()
print(channel)

```
###Note: replace your email-id and password on the email and password section 

####Example Output
```
SkypeGroupChat(id='19:b8aa1d14b9234***************6f09e7c@thread.skype'
```

### In second code we need to add the group chat id , to send the message automatically

```
from skpy import Skype
def post_message(msg,channel_id): 
  "Post a message" 
  sk = Skype("<email>","<password>")
  channel = sk.chats.chat("19:75a59852398*****************7aad872586@thread.skype") 
  channel.sendMsg(msg)
  print("Message Sent")

post_message("Good Morning!!","channel-id@thread.skype")

```

### This Code will create on group with users id that you have provided

```
from skpy import Skype
sk = Skype("<email>", "<password>") # connect to Skype

my_user = sk.user # you
my_contact = sk.contacts # your contacts
my_chats = sk.chats # your conversations


ch = sk.chats.create(["basnyatsumit.sb", "sagar_shrestha1212"]) # new group conversation users
##This are the username, i.e 
## First go to the user profile --> Skype Name --> live:username-example

print(my_user)
print(my_contact)
print(my_chats)

```

