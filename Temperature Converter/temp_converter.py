def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Select an option (1 or 2): ").strip()

    if choice in ("1", "2"):
        try:
            temp = float(input("Enter temperature to convert: "))

            if choice == "1":
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.2f}°F")
            else:
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.2f}°C")

        except ValueError:
            print("Invalid input! Please enter a numerical value.")
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()