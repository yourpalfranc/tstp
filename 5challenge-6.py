my_digits = {"height": "medium",
                     "weight": "180",
                     "hair": "gray",
                     "eyes": "blue",
                     }

n = input("Ask for my digits:")

if n in my_digits:
    display = my_digits[n]
    print(display)
else:
    print("Not a correct digit.")
