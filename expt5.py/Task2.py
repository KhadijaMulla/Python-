import re

text = input("Enter a paragraph: ")

sentences = re.split(r'(?<=[.!?])\s+', text)

print("Sentences:")
for sentence in sentences:
    print(sentence)