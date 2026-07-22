import random
import sys

def get_user_choice() -> str:
    """Prompts the user for a valid choice or exit command."""
    while True:
        choice = input("Enter Rock, Paper, Scissors (or 'exit' to quit): ").strip().lower()
        if choice == 'exit':
            print("Thanks for playing! Goodbye!")
            sys.exit()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please enter Rock, Paper, or Scissors.\n")

def play_game():
    options = ['rock', 'paper', 'scissors']
    
    print("=== Rock, Paper, Scissors Game ===")
    
    while True:
        user_choice = get_user_choice()
        # Now computer has to choise one of the option otherwise how should this game work
        computer_choice = random.choice(options)
        
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # 1. Check for a Tie
        if user_choice == computer_choice:
            print("It's a tie!\n")
            
        # Checking all the conditon for a mortal to win through a machine who only work on 0 and 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win!\n")
            
        # If nothing of the above condition happen mortal looses
        else:
            print("💻 Computer wins!\n")

if __name__ == "__main__":
    play_game()