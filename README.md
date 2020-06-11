# facebook-messenger-script
Made using [FBChat](https://github.com/carpedm20/fbchat "Thank you FBChat <3").
Sends text provided in a .txt file to a user on Facebook Messenger, word from word.

## Installing and Running Python
To install Python, please download the latest version for your OS from [the Python website](https://www.python.org/downloads/ "Love you Python <3"). If needed, follow the [specific instructions](https://realpython.com/installing-python/ "Python Installation") for installing Python for your OS. To ensure that Python works, open a command line and run `python --version` in the command prompt. If something like `Python 3.X.X` appears, then you've installed Python correctly and can move on to the next step.  

## Installing FBChat
In order to use this program, you must have the FBChat package installed. To do so, go to your command line and run `pip install fbchat`. If Pip is not installed for whatever reason, please follow the Pip [documentation](https://pip.pypa.io/en/stable/installing/ "Pip Installation") regarding installation.

## Editing Text to Send
By default, the text in `text.txt` sends the entire Bee Movie Script. However, feel free to edit the file to send whatever you want.

## Logging In
In order to log in, please create a `credentials.txt` file in the `facebook-messenger-script` directory (you can do this by going to the command line, navigating to the `facebook-messenger-script` directory, and running `touch credentials.txt`). Then, in the first line of the file, enter your Facebook email. In the second line, enter your Facebook password.

## Finding Facebook Users' IDs and Sending a Message
Before sending the messages, open a command line, navigate to the `facebook-messenger-script` directory, and run `python search.py`. Follow the instructions to search for a person on Facebook and send your messages to them (**Note**: a good way to distinguish the person you're searching for from other people is to verify their profile picture and check that the person is your friend).

For more information, please refer to the [documentation](https://fbchat.readthedocs.io/en/stable/examples.html#fetching-information "FBChat Docs") regarding looking up Facebook users' IDs.

## Manually Sending the Message
If you already have a user ID to send your messages to, run `python message.py <user_id>`, where `<user_id>` is the user ID to send to.