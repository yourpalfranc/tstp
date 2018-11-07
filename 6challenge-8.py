#Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a gramatically
#correct string. There should be a space between each word, but no space between the word
#fence and the period that follows it. (Don't forget you learned a method that turns a list into a
#single string.

my_quote = ["The",
                        "fox",
                        "jumped",
                        "over",
                        "the",
                        "fence",
                        "."] 
my_quote = " ".join(my_quote)
my_quote = my_quote[0:-2] + "."

print(my_quote)


