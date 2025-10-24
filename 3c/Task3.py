vowels = 0
consonants = 0

user_input = input("Enter text")

for char in user_input:
    if char.isalpha:
        char.lower()
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1


print(f"Vowels: {vowels}, Consonants: {consonants}")
