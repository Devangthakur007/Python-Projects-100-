import sys

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts text using the Caesar cipher technique.
    - text: The message to transform
    - shift: Number of positions to shift
    - mode: 'encript' or 'decrypt' 
    """

    result = ""

    # if decrypting, reverse the shift direction
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Convert letter to 0-25 index using ASCII value (ord('A') = 65)
        shifted = (ord(char) - ord('a') + shift) % 26
        result += chr(shifted +ord('a'))



    # Leave numbers, spaces, and punctuation untouched
    else:
        result += char

    return result

def main():
    print("=== Caesar Cipher tool ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        action = input("Do you want to (E)ncrypt, (D)ecrypt, or 'exit'? ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            sys.exit()

        if action not in ['e', 'encript', 'd', 'decrypt']:
            print("Invalid choice! Choose 'e' for encrypt or 'd' for decrypt\n")
            continue

        mode = 'encript' if action in ['e' , 'eccrypt'] else 'decrypt'
        message = input("Enter your message: ").strip()

        # GEt valid shift key
        while True:
            shift_input = input("Enter shift number (e.g., 3: )").strip()
            if shift_input.lower() == 'exit':
                print("Goodbye!")
                sys.exit()
            try:
                shift_key = int(shift_input)
                break
            except ValueError:
                print(" Invalid shift! Please enter a whole number.")

        output = caesar_cipher(message, shift_key, mode)

        print(f"\n Result ({mode.capitalize()}ed): {output}\n")
        print("-" * 40)

if __name__ == " __main__":
    main


