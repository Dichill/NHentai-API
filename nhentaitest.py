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
