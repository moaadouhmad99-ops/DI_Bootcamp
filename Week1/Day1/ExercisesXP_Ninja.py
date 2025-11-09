##  Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
#  >>> 3 <= 3 < 9
print(3 <= 3 < 9)  # True, because 3 is equal to 3 and less than 9
#  >>> 3 == 3 == 3 
print(3 == 3 == 3)  # True, because all three values are equal
#  >>> bool(0)
print(bool(0))  # False, because 0 is considered False in boolean context
#  >>> bool(5 == "5")
print(bool(5 == "5"))  # False, because integer 5 is not equal to string "5"
#  >>> bool(4 == 4) == bool("4" == "4")
print(bool(4 == 4) == bool("4" == "4"))  # True, because both sides evaluate to True
#  >>> bool(None)
print(bool(None))  # False, because None is considered False in boolean context
#  x = (1 == True)
print(1==True)  # True, because 1 is considered equal to True
#  y = (1 == False)
print(1==False)  # False, because 1 is not equal to False
#  a = True + 4
print(True + 4)  # 5, because True is treated as 1 in arithmetic operations
#  b = False + 10
print(False + 10)  # 10, because False is treated as 0 in arithmetic operations

#############################################################################
###############################################################################
##  Exercise 4 : How many characters in a sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))


#############################################################################
###############################################################################
##  Exercise 5: Longest word without a specific character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
longest_sentence = ""
while True:
    sentence = input("Please enter the longest sentence you can without the character 'A': ")
    if 'A' in sentence.upper():
        print("Your sentence contains the character 'A'. Please try again.")
    else:
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence
            print("Congratulations! You've set a new longest sentence.")
        else:
            print("Your sentence is not longer than the current longest sentence. Please try again.")
