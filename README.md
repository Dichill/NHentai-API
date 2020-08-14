# NHentai API | The God's Language.

## Features

* **Easy Code Checker!**
* **Only needs BS4 and Requests!**
* **Get Previews and Tags in just a matter of seconds!**

# Try it!
<iframe height="400px" width="100%" src="https://repl.it/repls/LegitimateScentedTypes?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

## How to Use

```python
# This can also be found in nhentaitest.py
# Author Dichill
# Please delete the folders on "Image/preview/ when using the same code on getPreviews it will give an error statement
# My lazy ass wont fix it, theres a lot of room for improvement, so please if you have some spare time dont mind snipping my code
# but atleast give some credits c:
# Enjoy.

import importlib
import os
api = importlib.import_module('nhentaiapi')
drx = api.nhentai()

os.system("cls")
os.system("color c")
print("Author: Dichill | API Author: Dichill")
print("Compatible with Discord Bot with Slight Modification.")
a = input("Paste Code Here: ") # PUT YOUR CODE

# Check the Code if it Works!
drx.check(a)

b = input("Do you want to check the Tags?: ")
os.system("cls")
c = input("Would you like to have some previews?: ")
os.system("cls")

if b == 'y' or 'yes' or 'Yes':
    print("==============================================")
    print("Tags")
    print("==============================================")
    drx.getTags(a)

if c == 'y' or 'yes' or 'Yes':
    d = input("How many Previews would you like? If there are less than the previews it will automatically end the process. ")
    drx.getPreviews(a, 20)

```

## Documentation
Coming Soon!
