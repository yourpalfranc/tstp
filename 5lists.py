colors = ["purple", "orange", "green"]

print(colors)

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again!!")
