import sys

def generate_fibonacci(n: int) -> list[int]:
    """Generates a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Start sequence with 0 and 1
    fib = [0, 1]
    
    # Generate numbers iteratively
    for i in range(2, n):
        next_val = fib[-1] + fib[-2]
        fib.append(next_val)
        
    return fib


def main():
    print("===  Fibonacci Sequence Generator ===")
    
    while True:
        user_input = input("\nEnter how many terms you want (or 'exit'): ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
            
        try:
            count = int(user_input)
            if count <= 0:
                print(" Please enter a positive integer.")
                continue
                
            sequence = generate_fibonacci(count)
            print(f"\n First {count} terms:")
            print(sequence)
            
        except ValueError:
            print(" Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()