#Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(12)


CAESAR GAME
# Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function to encrypt or decrypt
def caesar(text, shift_amount, mode):
    result_text = ""
    if mode == "decode":
        shift_amount *= -1  # reverse shift for decoding

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            result_text += alphabet[new_position]
        else:
            result_text += letter  # keep non-alphabet characters as-is

    print(f"Here's the {mode}d result: {result_text}")

# Call the function
caesar(text, shift, direction)

