import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # Special characters like !@#$%^&*

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))

