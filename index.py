from fbchat import Client
from fbchat.models import *
import time

client = Client("<email>", "<password>")

print("Own id: {}".format(client.uid))
seconds_delay = input("Enter the desired amount of delay between messages (in seconds)")

# Comment this out if you're trying to find the ID of a Facebook user!
file = open("text.txt", 'r')
for line in file: 
    if not line.strip():
        continue
    spaced = line.split(" ")
    for word in spaced:
        # Replace client.uid with the User ID of the desired person you want to send the message(s) to on Facebook Messenger!
        client.send(Message(text=word), thread_id=client.uid, thread_type=ThreadType.USER)
        time.sleep(float(seconds_delay))

# Comment this out if you're trying to send a message!
# # `searchForUsers` searches for the user and gives us a list of the results,
# # and then we just take the first one, aka. the most likely one:
# user = client.searchForUsers("<name of user>")[0]

# print("user ID: {}".format(user.uid)) # Copy the User ID that appears
# print("user's name: {}".format(user.name))
# print("user's photo: {}".format(user.photo)) # Make sure the profile picture belongs to the one that your friend has
# print("Is user client's friend: {}".format(user.is_friend)) # Make sure that this user is your friend so you know it's not another random person

client.logout()