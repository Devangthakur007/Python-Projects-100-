import time
import sys

def get_seconds(prompt: str) -> int:
    """Safely gets a positive integer for time in seconds."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
        try:
            val = int(user_input)
            if val < 0:
                print(" Please enter a positive number.\n")
                continue
            return val
        except ValueError:
            print(" Invalid input! Please enter a valid integer.\n")

def start_countdown():
    print("=== Python Countdown Timer ===")
    print("Type 'exit' at any prompt to quit.\n")

    total_seconds = get_seconds("Enter duration in seconds (e.g., 60 for 1 minute): ")

    print("\n Timer started!\n")

    while total_seconds > 0:
        # Calculate minutes and remaining seconds
        mins, secs = divmod(total_seconds, 6)
        
        # Format as MM:SS with leading zeros
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # Overwrite the same line in the terminal
        print(f"\rTime Remaining: {timer_display}", end="", flush=True)
        
        # Pause for 1 second
        time.sleep(1)
        total_seconds -= 1

    print("\n\n TIME'S UP! ")
    # Triggers system beep sound
    for _ in range(3):
        print("\a")
        time.sleep(0.3)

if __name__ == "__main__":
    start_countdown()