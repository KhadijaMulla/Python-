s = input("Enter a string: ")

print("\nOriginal String:", s)

print("\n1. Length:", len(s))
print("2. Uppercase:", s.upper())
print("3. Lowercase:", s.lower())
print("4. Capitalize:", s.capitalize())
print("5. Title:", s.title())
print("6. Swapcase:", s.swapcase())
print("7. Reverse:", s[::-1])

if s == s[::-1]:
    print("8. Palindrome: Yes")
else:
    print("8. Palindrome: No")

ch = input("\nEnter character to count: ")
print("9. Count:", s.count(ch))

ch = input("Enter character to find: ")
print("10. Find Index:", s.find(ch))

old = input("Enter character/word to replace: ")
new = input("Enter new character/word: ")
print("11. Replace:", s.replace(old, new))

print("12. Split:", s.split())

joined = "-".join(s)
print("13. Join with '-':", joined)

start = input("Enter prefix: ")
print("14. Startswith:", s.startswith(start))

end = input("Enter suffix: ")
print("Endswith:", s.endswith(end))

print("15. Remove Spaces:", s.replace(" ", ""))

print("16. Is Alphabet:", s.isalpha())
print("17. Is Digit:", s.isdigit())
print("18. Is Alphanumeric:", s.isalnum())

s2 = input("\nEnter another string to compare: ")

if s == s2:
    print("19. Strings are Equal")
else:
    print("19. Strings are Not Equal")

print("20. Concatenation:", s + " " + s2)

rot = int(input("\nEnter rotation value: "))

left_rotation = s[rot:] + s[:rot]
right_rotation = s[-rot:] + s[:-rot]

print("21. Left Rotation:", left_rotation)
print("    Right Rotation:", right_rotation)

choice = int(input("""
21. Password Validator
22. Run-Length Encoding
23. String Compression
24. Most Frequent Character
25. Second Most Frequent Character
26. Caesar Cipher
27. Email Validator
28. Word Frequency Dictionary
29. Sentence Reversal
30. String Rotation
Enter choice: """))

if choice == 21:
    s = input("Enter Password: ")
    upper = lower = digit = special = 0

    for ch in s:
        if ch.isupper():
            upper = 1
        elif ch.islower():
            lower = 1
        elif ch.isdigit():
            digit = 1
        else:
            special = 1

    if len(s) >= 8 and upper and lower and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")

elif choice == 22:
    s = input("Enter String: ")
    result = ""
    count = 1

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    print(result)

elif choice == 23:
    s = input("Enter String: ")
    result = ""
    count = 1

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    if len(result) < len(s):
        print(result)
    else:
        print(s)

elif choice == 24:
    s = input("Enter String: ")
    max_count = 0
    result = ""

    for ch in s:
        count = s.count(ch)
        if count > max_count:
            max_count = count
            result = ch

    print("Most Frequent Character:", result)

elif choice == 25:
    s = input("Enter String: ")
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    values = sorted(set(freq.values()), reverse=True)

    if len(values) < 2:
        print("No Second Most Frequent Character")
    else:
        second = values[1]

        for ch in s:
            if freq[ch] == second:
                print("Second Most Frequent Character:", ch)
                break

elif choice == 26:
    s = input("Enter Message: ")
    shift = int(input("Enter Shift: "))
    result = ""

    for ch in s:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch

    print("Encrypted:", result)

elif choice == 27:
    email = input("Enter Email: ")

    if "@" in email and "." in email and email.index("@") < email.rindex("."):
        print("Valid Email")
    else:
        print("Invalid Email")

elif choice == 28:
    s = input("Enter Paragraph: ")
    words = s.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print(freq)

elif choice == 29:
    s = input("Enter Sentence: ")
    words = s.split()
    result = ""

    for word in words:
        result = word + " " + result

    print(result)

elif choice == 30:
    s1 = input("Enter First String: ")
    s2 = input("Enter Second String: ")

    if len(s1) == len(s2) and s2 in s1 + s1:
        print("Yes")
    else:
        print("No")

else:
    print("Invalid Choice")