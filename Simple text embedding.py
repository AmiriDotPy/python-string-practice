# Algorithm:
# 1. Get a sentence from the user.
# 2. Get the old word and the new word.
# 3. Replace the first occurrence of the old word.
# 4. Convert the result to uppercase.
# 5. Reverse the result and print it.
#
# Example Input:
# Text: python is easy
# Old word: easy
# New word: powerful
#
# Full Output:
# LAREWOP SI NOHTYP


print("We are going to take a text from you and replace one of its words with another word, so...")

text = input("Enter the entire sentence you have in mind: ")
old_word = input("Enter The old word you will enter into the text :")
new_word = input("Enter the word you want to replace: ")

print(text.replace(old_word, new_word, 1).upper()[::-1])

# Alternative: chain all string operations directly after input().
# Kept as a reference for method chaining.
# text = input("Now, enter the entire sentence you have in mind: ").replace(old_word, new_word, 1).upper()[::-1]
# print(text)


