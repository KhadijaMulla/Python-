import re

dictionary = {
    "this", "is", "a", "simple", "python",
    "program", "hello", "world", "good", "day"
}

text = input("Enter the text: ")

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

misspelled = []

for word in words:
    if word not in dictionary:
        misspelled.append(word)

print("Misspelled words:", misspelled)