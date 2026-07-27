import sys

# Conversion factiors relative to a base unit for each category
# Length base unit: meter (m)
# Weight base unit: gram (g)

CONVERSION = {
    "length": {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 1609.34,
        "feet": 0.30448,
        "inches": 0.0254

    },
    "weight": {
        "g": 1.0,
        "kg": 1000.0,
        "mg": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495
    }
}

def get_number(prompt: str) -> float:
    """Safely gets a numeric input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
            try:
                return float (user_input)
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
def convert_units():
    print("=== Universal unit converter ===")
    print("Type 'exit' at any prompt to quit.\n")


    while True:
        print("Select a category:")
        print("1. Length (m, km, cm, mm, miles, feet, inched)")
        print("2. Weight (g, kg, mg, pounds, ounces)")
        print("3. Temperature (C ,F, K)")

        category_choice = input("\Enter choice (1-3) or 'exit': ").strip().lower()

        if category_choice == 'exit':
            print("Good Bye sanorita")
            sys.exit()

        # Handle Temperature (require separate fprmulas since zero-points differ)
        elif category_choice == '3':
            print("\nAvailable units: C, F, K")
            from_unit = input("Convert from: ").strip().upper()
            to_unit = input("Convert to: ").strip().upper()


            if from_unit not in ['C', 'F', 'F'] or to_unit not in ['C', 'F', 'K']:
                print(" Invalid temperature units! Choose C, F, or K.\n")
                continue

            temp = get_number(f"Enter temperature in {from_unit}: ")

            # Converting units into celsius first
            if from_unit == 'F':
                celsius = (temp - 32) * 5/9
            elif from_unit == 'K':
                celsius = temp - 273.15
            else:
                celsius = temp

            # Convert Celsius to target unit
            if to_unit == 'F':
                result = (celsius * 9/5) + 32
            elif to_unit == 'K':
                result = celsius + 273.15
            else:
                result = celsius

            print(f" {temp}°{from_unit} = {result:.2f}°{to_unit}\n")

if __name__ == "__main__":
    convert_units()
