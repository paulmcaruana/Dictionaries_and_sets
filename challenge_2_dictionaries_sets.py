# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

words = set(input("Please input some text here: "))
vowels = {"a", "e", "i", "o", "u"}

print(words.difference(vowels))

#tim's answer

sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou") #quicker than my answer
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalSet = sorted(finalSet)
print(finalSet)
