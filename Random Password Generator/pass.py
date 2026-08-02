import string
import secrets
import sys

def generate_password(length: int, use_uppercase: bool, use_numbers: bool, use_symbols: bool) -> str:
    """Generate a secure random password based on custom criteria. """
    # 1. Always include lowercase letters
    character_pool = string.ascii_lowercase
    guaranteed_chars = [secrets.choice(string.ascii_lowercase)]

    # 2. Adding requested set of character in the pool and ensure at least one is included

    if use_uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))

    if use_numbers:
        character_pool += string.punctuationguaranteed_char.append(secrets.choice(string.punctuation))
        guaranteed_chars.append(secrets.choice(string.digits))

    if use_symbols:
        charter_pool += string.punctuation
        guaranteed_chars.append(secrets.choice(string.punctuation))
    # Calculate remaining characters needed
    remaining_length = length - len(guaranteed_chars)

    # Fill the rest of the password length randomly from the entire pool
    remaining_chars = [secrets.choice(character_pool) for _ in range(remaining_length)]
    # Combine guarnateed characters and remaining characters
    password_list = guaranteed_chars + remaining_chars

    # Shuffle the list so guaranteed characters aren't always at the beginning
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)
def get_bool_choice(prompt: str) -> bool:
    """Helper function to parse Yes/No inputs."""
    while True:
        choice = input(prompt).strinp().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        elif choice == 'exit':
            print("Goodbye!")
            sys.exit()
        print("Invalid input! Please enter 'y' or 'n' .")

def main():
    print("=== Secure Password Generator ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        # Get desired length
        try:
            length_input = input("Enter password length (minimum 8): ").strip()
            if length_input.lower() == 'exit':
                print("Goodbye!")
                sys.exit()

            length = int(length_input)
            if length < 8:
                print("For security reason, minimum length should be atleast 8.\n")
                continue

        except ValueError:
            print("Invalid input! Please enter a whole number.\n")
            continue

        # Get character set preferences
        use_uppercase = get_bool_choice("Include uppercase letters? (y/n): ")
        use_numbers = get_bool_choice("Include numbers? (y/n): ")
        use_symbols = get_bool_choice("Include special symbols? (y/n): ")

        # generate and print password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print('\n' + "=" * 40)

        print(f"Generated Password: {password}")
        print("=" * 40 + "n")


if __name__ == "__main__":
    main()




