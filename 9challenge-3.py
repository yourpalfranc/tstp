#Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
#"The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] and write them to a .csv file.
#The data from each list should be a row in the file, with each item in the list seperated by a comma.

import os
import csv

mydir = os.path.join(os.sep, "home", "frank", "Documents", "self-taught", "ch9-challenge")
myfile = os.path.join(os.sep, "movies.csv")
mypath = mydir + myfile
#print(mypath)

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
#for i in movies:
#    print(i)

with open(mypath, "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for actor in movies:
        w.writerow(actor)
