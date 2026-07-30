import sys

def is_leap_year(year: int) -> bool:
    """Checks if a year is a leap year based on Gregorian calender rules."""
    # Divisible by 400 -> Always a leap year
    if year % 400 == 0:
        return True
    # Divisible by 100 -> Not a lear year
    if year % 100 == 0:
        return False
    # Divisible by 4 -> Leap year
    if year % 4 ==0:
        return True

    return False


def main():
    print("=== Python Leap Year Checker ===")
    print("Type 'exit' at any prompt to quit.\n")


    while True:
        user_input = input("Enter a year (e.g., 2024): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()

        try:
            year = int(user_input)
            if year <= 0:
                print("Please enter a valid positive year! (366 days)\n")
                continue


            if is_leap_year(year):
                print(f"{year} Is a leap year! (366 days)\n")
            else:
                print(f" {year}is not a leap year. (365 days)\n")

            print("-" * 40)

        except ValueError:
            print("Invalid input! Please enter a whole number for the year.\n")


if __name__ == "__main__":
    main()


