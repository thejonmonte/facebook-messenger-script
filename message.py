from fbchat import Client
from fbchat.models import *
import time
import auth
import sys

def send(uid, client):
    seconds_delay = input("\nEnter the desired amount of delay between messages (in seconds)\n")
    file = open("text.txt", "r")
    for line in file: 
        if not line.strip():
            continue
        spaced = line.split(" ")
        for word in spaced:
            client.send(Message(text=word), thread_id=uid, thread_type=ThreadType.USER)
            time.sleep(float(seconds_delay))

def main():
    if len(sys.argv) == 1:
        print("Please enter a user ID to send messages to.")
        sys.exit()

    client = auth.login()
    uid = sys.argv[1]
    send(uid, client)

if __name__ == "__main__":
    main()