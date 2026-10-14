text = input("Enter the text: ")
query = input("Enter the word to search: ")

count = text.lower().count(query.lower())

highlighted = text.replace(query, "**" + query + "**")

print("Number of occurrences:", count)
print("Highlighted text:", highlighted)
