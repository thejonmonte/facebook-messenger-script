# facebook-messenger-script
Made using [FBChat](https://github.com/carpedm20/fbchat "Thank you FBChat <3").
Sends text provided in a .txt file to a user on Facebook Messenger, word from word.

## Finding Facebook Users' IDs
Before sending the message, follow the instructions in `index.py` for finding the User ID for a Facebook user (I.E. uncomment the `search` code, comment out the `send` code, replace `<name of user>` with the desired Facebook username, run `python index.py`, and make sure the user is one of your friends and not a random person). For more information, please refer to the [documentation regarding looking up Facebook users' IDs](https://fbchat.readthedocs.io/en/stable/examples.html#examples "FBChat Docs"), specifically the **Fetching Information** section.

## Sending the Message
In order to send the message, in `index.py`, make sure that the `send` code is uncommented and the `search` code is commented. Replace `<email>` and `<password>` with your Facebook email and password. Then replace the `thread_id` argument in `Message()` with the User ID found in the previous section. `cd` into the `facebook-messenger-script` and run `python index.py`. Specify the amount of delay (in seconds) between messages and **voila!** An annoying Facebook spam chat bot!
