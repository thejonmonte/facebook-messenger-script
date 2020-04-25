# facebook-messenger-script
Made using [FBChat](https://github.com/carpedm20/fbchat "Thank you FBChat <3").
Sends text provided in a .txt file to a user on Facebook Messenger, word from word.

## Finding Facebook Users' IDs
Before sending the message, please refer to the [documentation regarding looking up Facebook users' IDs](https://fbchat.readthedocs.io/en/stable/examples.html#examples "FBChat Docs").

## Sending the Message
In order to send the message, in index.py, replace `<email>` and `<password>` with your Facebook email and password. Then use the above documentation to find the User ID(s) of the desired person/group. `cd` into the `facebook-messenger-script` and run `python index.py`. Specify the amount of delay (in seconds) between messages and **voila!** An annoying Facebook spam chat bot!
