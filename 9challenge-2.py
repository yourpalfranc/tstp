#Write a program that asks a user a question, an saves their answer to a file.

import os
mypath = os.path.join(os.sep, "home", "frank", "Documents", "self-taught", "ch9-challenge", "newfile2.txt")

contents = input("What would you like to add to the file?: ")
#contents = """ + contents + """

#print(contents)

with open(mypath, "w") as f:
    f.write(contents)
