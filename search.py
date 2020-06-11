from fbchat import Client
from fbchat.models import *
import message
import auth
import sys

def displayOptions(index, client, users):
    while True:
        option = input("\nWhat would you like to do?\n").strip().lower()

        if option == "c":
            return -2
        else:
            if not option:
                return index + 1
            elif option == "b":
                if index > 0:
                    return index - 1
            elif option == "s":
                message.send(users[index].uid, client)
            elif option == "q":
                client.logout()
                sys.exit()
            else:
                print("\nPlease enter a valid command.")
                continue
            return -1

def main():
    client = auth.login()

    while True:
        personToSearch = input("\nPlease enter the name of the person that you want to search.\n").strip()

        # `searchForUsers` searches for the user and gives us a list of the results,
        # and then we just take the first one, aka. the most likely one:
        index = 0
        users = client.searchForUsers(personToSearch)

        print("\nOptions:")
        print("Press 'Enter' to see the next user")
        print("Type 'b' to see the previous user")
        print("Type 's' to send your messages to this user")
        print("Type 'c' to continue searching for another person")
        print("Type 'q' to quit the program\n")

        while True:
            if index == len(users):
                print("All search results for this person have been shown.")
                break

            print("User ID: {}".format(users[index].uid)) # Copy the User ID that appears
            print("User's name: {}".format(users[index].name)) # Show the Facebook user's username
            print("User's photo: {}".format(users[index].photo)) # Make sure the profile picture belongs to the one that your friend has
            print("Is user client's friend: {}".format(users[index].is_friend)) # Make sure that this user is your friend so you know it's not another random person

            option = displayOptions(index, client, users)
            if option == -2:
                break
            elif option >= 0:
                index = option

if __name__ == "__main__":
    main()