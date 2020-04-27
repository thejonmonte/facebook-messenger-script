# facebook-messenger-script
Made using [FBChat](https://github.com/carpedm20/fbchat "Thank you FBChat <3").
Sends text provided in a .txt file to a user on Facebook Messenger, word from word.

## Installing and Running Python
To install Python, please download the latest version for your OS from [the Python website](https://www.python.org/downloads/ "Love you Python <3"). If needed, follow the [specific instructions](https://realpython.com/installing-python/ "Python Installation") for installing Python for your OS. To ensure that Python works, open a command line and run `python --version` in the command prompt. If something like `Python 3.X.X` appears, then you've installed Python correctly and can move on to the next step.  

## Installing FBChat
In order to use this program, you must have the FBChat package installed. To do so, go to your command line and run `pip install fbchat`. If Pip is not installed for whatever reason, please follow the [Pip documentation regarding installation](https://pip.pypa.io/en/stable/installing/ "Pip Installation").

## Logging In
In order to log in, please create a `credentials.txt` file in the `facebook-messenger-script` directory (you can do this by going to the command line and running `touch credentials.txt`). Then, in the first line of the file, enter your Facebook email. For the second line, enter your Facebook password.

## Finding Facebook Users' IDs
Before sending the message, follow the instructions in `index.py` for finding the User ID for a Facebook user (I.E. uncomment the `search` code, comment out the `send` code, replace `<name of user>` with the desired Facebook username, run `python index.py`, and make sure the user is one of your friends and not a random person). For more information, please refer to the [documentation regarding looking up Facebook users' IDs](https://fbchat.readthedocs.io/en/stable/examples.html#examples "FBChat Docs"), specifically the **Fetching Information** section.

## Sending the Message
In order to send the message, in `index.py`, make sure that the `send` code is uncommented and the `search` code is commented. Replace the `thread_id` argument in `Message()` with the User ID found in the previous section. `cd` into the `facebook-messenger-script` and run `python index.py`. Specify the amount of delay (in seconds) between messages and **voila!** An annoying Facebook spam chat bot!
