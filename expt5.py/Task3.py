import re

text = input("Enter a word or phrase: ")

# Remove spaces and punctuation
cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

if cleaned == cleaned[::-1]:
    print("True - It is a palindrome")
else:
    print("False - It is not a palindrome")