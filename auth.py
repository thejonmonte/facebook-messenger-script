from fbchat import Client
from fbchat.models import *

def login():
    creds = open("credentials.txt", 'r')
    creds_lines = creds.readlines()

    user = creds_lines[0].strip()
    password = creds_lines[1].strip()

    return Client(user, password)