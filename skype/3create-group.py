from skpy import Skype
sk = Skype("<email>", "<password>") # connect to Skype

my_user = sk.user # you
my_contact = sk.contacts # your contacts
my_chats = sk.chats # your conversations


ch = sk.chats.create(["basnyatsumit.sb"]) # new group conversation users. You can add multiple users
##This are the username, i.e
## First go to the user profile --> Skype Name --> live:username-example

print(my_user)
print(my_contact)
print(my_chats)


