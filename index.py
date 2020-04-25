from fbchat import Client
from fbchat.models import *
import time

client = Client("<email>", "<password>")

print("Own id: {}".format(client.uid))
seconds_delay = input("Enter the desired amount of delay between messages (in seconds)")

file = open("text.txt", 'r')
for line in file: 
    if not line.strip():
        continue
    spaced = line.split(" ")
    print(spaced)
    for word in spaced:
        # Replace client.uid with ID of the desired person you want to send the message(s) to on Facebook Messenger!
        client.send(Message(text=word), thread_id=client.uid, thread_type=ThreadType.USER)
        time.sleep(float(seconds_delay))

client.logout()