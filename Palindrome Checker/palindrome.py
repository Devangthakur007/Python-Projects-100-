import sys
import string

def is_palindrome(text: str) -> bool:
    """
    Checks if a string is a palindrome.
    Ignores casing, spaces, and punctuation.
    """

    # Clean the string: convert to lowercase and keep only alphanumberic characters

    cleaned_text = "".join(char.lower() for char in text if char.isalnum())

    # Check if the cleaned string is empty
    if not cleaned_text:
        return False
    # Compare string with its reverse useing Python slicing[::-1]
    return cleaned_text == cleaned_text[::-1]

def main():
    print("=== Python Palindrome Checker ===")
    print("Type 'ext' at any prompt to quit.\n")

    while True:
        user_input = input("Enter a word, pharase, or number: ").strip()

        if user_input.lower() =='exit':
            print("Goodbye!")
            sys.exit()

            if not user_input:
                print("Input cannot be Empty")
                continue

            if is_palindrome(user_input):
                print(f" Yes! '{user_input}' is a palindrome!\n")
            else:
                print(f"NO. '{user_input}' is not a palindrome.\n")

            print("-" * 45)


if __name__ == "__main__":
    main()