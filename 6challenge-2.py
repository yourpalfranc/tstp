#Write a program that collects two strings from a user, inserts them into the string "Yesterday
#I wrote a {response_one}. I sent it to {response_two}" and prints a new string

response_one = input("Enter a type of correspondence:")
response_two = input("Enter the recipient's name:")

r = "Yesterday I wrote a {}. I sent it to {}".format(response_one, response_two)
print(r)


