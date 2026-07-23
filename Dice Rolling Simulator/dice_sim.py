import random 

def roll_dice():

    return random.randint(1, 6)

def main():
    print("---Welcome to the Soul Socity of Dice Roller! ---")

    while True:
        user_input = input("\nPress [Enter] to roll the die (or type 'q' to quit):").strip().lower()

        if user_input == 'q':
            print("Thanks for playing! Goodbye. ")
            break
        result = roll_dice()
        print(f" You rolled a: {result}")

if __name__ == "__main__":
    main()
