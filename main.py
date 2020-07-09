# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:

#   My name is Gabriel
# Then I would see the string:

#   Gabriel is name My
# shown back to me.


def main():
    userInput = str(input("Type a sentence: "))

    userInput = userInput.split()
    userInput = userInput[::-1]
    userInput = " ".join(userInput)

    print("Your reverse sentence should be: " + userInput)


main()
