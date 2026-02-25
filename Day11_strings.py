#program1:basic of string
text = "Python Programming"

print(text.lower())
print(text.upper())
print(len(text))
print(text[0])
print(text[-1])

#program2:loop and string
text = "Python"

for ch in text:
    print(ch)

#program3:reverse string
text = input("Enter text: ")

rev = text[::-1]
print("Reverse:", rev)

#program4:palidrome
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

#program5:counting words
sentence = input("Enter sentence: ")

words = sentence.split()
print("Word count:", len(words))

#program6:counting character
text = input("Enter text: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

#program7:email verification
email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
