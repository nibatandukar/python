from skpy import Skype
email = "<email>"
password = "<password>"
sk = Skype("<email>","<password>")
channel = sk.chats.recent()
print(channel)

###Note: replace your email-id and password on the email and password section
