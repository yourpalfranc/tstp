#return a random word from a list

import random

def the_word():
    wordlist = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf",
                "hotel", "india", "juliette", "kilo", "lima", "mike", "november",
                "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform"
                "victor", "whiskey", "xray", "yankee", "zebra"]
    randomnumber = random.randint(0,25)
    return(wordlist[randomnumber])
#print(randomnumber)
#randomnumber = randomnumber - 1
#print(randomnumber)
