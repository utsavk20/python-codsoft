import random
import string

# Define a function to generate a password
def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Check if the user wants to include all character types
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Create a string of allowed characters based on user input
    allowed_characters = ""
    if use_uppercase:
        allowed_characters += string.ascii_uppercase
    if use_numbers:
        allowed_characters += string.digits
    if use_special_chars:
        allowed_characters += string.punctuation
    if not allowed_characters:
        allowed_characters = string.ascii_lowercase

    # Generate the password
    password = ''.join(random.choice(allowed_characters) for _ in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate and display the password
password = generate_password(length)
print("Generated Password : ", password)
