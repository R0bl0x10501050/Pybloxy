# Pybloxy

A Python API wrapper for Roblox services.

Pybloxy is a Python API wrapper for the Roblox API. You can use this for bots, websites, you name it!

# Setup

First, install the Pybloxy package.

```
pip install pybloxy
```

Next, make sure to import **which services you need.** For example:

```py
from Pybloxy import User
```

Finally, make sure to **log in** to your bot account with the login command.

```py
from Pybloxy import User

User.login("token") # scroll down for info about making your tokens private
```

You're all set! Below is a list of the classes:
* Assets
* Friends
* Groups
* User
* More Coming Soon...

# Use ENV!

If you're one who wouldn't like everyone being able to see your token, then use an ENV file.

1. Create a new file in your main tree called `.env`
2. In the `.env` file, paste exactly this but replace `TokenHere` with your token.
```env
RBLXTOKEN=TokenHere
```
3. Now, when you log in to your bot, just do this:
```py
from Pybloxy import Users

User.login(os.getenv("RBLXTOKEN"))
```

> Quick Side Note: No one but you and people who are part of your project can see the contents of ENV files. Make sure to not add random people & stay safe!

# Credit

1. Credit to Pyblox, the module Pybloxy is based off of.
2. R0bl0x10501050 - Lead Maintainer