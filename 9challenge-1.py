#Find a file on your computer and print its contents using Python

import os
mypath = os.path.join(os.sep, "home", "frank", "Documents", "self-taught", "ch9-challenge", "newfile.txt")

with open(mypath, "r") as f:
    print(f.read())
