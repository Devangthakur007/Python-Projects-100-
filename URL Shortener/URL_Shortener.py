import hashlib
import json
import os
import re
import sys
import webbrowser

DATA_FILE = "urls.json"
BASE_DOMAIN = "http://short.ly/"

def load_data() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

def save_data(data: dict):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except OSError as e:
        print(f"Error saving data: {e}")

def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None

def generate_short_code(original_url: str, length: int = 6) -> str:
    sha = hashlib.sha256(original_url.encode()).hexdigest()
    return sha[:length]

def shorten_url(data: dict):
    url = input("Enter the long URL: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    if not is_valid_url(url):
        print("Invalid URL format.")
        return

    for code, info in data.items():
        if info["original_url"] == url:
            print(f"\nExisting short URL: {BASE_DOMAIN}{code}")
            return

    custom_alias = input("Enter custom alias (press Enter to auto-generate): ").strip()
    if custom_alias:
        if not custom_alias.isalnum():
            print("Custom alias must be alphanumeric.")
            return
        if custom_alias in data:
            print("Alias already in use. Please choose another.")
            return
        code = custom_alias
    else:
        code = generate_short_code(url)
        counter = 1
        original_code = code
        while code in data and data[code]["original_url"] != url:
            code = f"{original_code}{counter}"
            counter += 1

    data[code] = {
        "original_url": url,
        "clicks": 0
    }
    save_data(data)
    print(f"\nShortened URL: {BASE_DOMAIN}{code}")

def redirect_url(data: dict):
    short_input = input("Enter short code or full short URL: ").strip()
    code = short_input.replace(BASE_DOMAIN, "").strip()

    if code not in data:
        print("Short code not found.")
        return

    original_url = data[code]["original_url"]
    data[code]["clicks"] += 1
    save_data(data)

    print(f"Redirecting to: {original_url}")
    open_browser = input("Open in default browser? (y/n): ").strip().lower()
    if open_browser in ["y", "yes"]:
        webbrowser.open(original_url)

def view_analytics(data: dict):
    if not data:
        print("\nNo URLs tracked yet.")
        return

    print("\n--- URL ANALYTICS ---")
    for code, info in data.items():
        print(f"Short URL : {BASE_DOMAIN}{code}")
        print(f"Target    : {info['original_url']}")
        print(f"Clicks    : {info['clicks']}")
        print("-" * 30)

def delete_url(data: dict):
    short_input = input("Enter short code to delete: ").strip()
    code = short_input.replace(BASE_DOMAIN, "").strip()

    if code not in data:
        print("Short code not found.")
        return

    del data[code]
    save_data(data)
    print(f"Deleted short code: '{code}'")

def main():
    data = load_data()
    print("=== URL Shortener ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        print("\nMenu:")
        print("1. Shorten URL")
        print("2. Expand / Access URL")
        print("3. View Analytics")
        print("4. Delete Short URL")
        print("5. Exit")

        choice = input("\nSelect option (1-5): ").strip().lower()

        if choice in ["5", "exit"]:
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            shorten_url(data)
        elif choice == "2":
            redirect_url(data)
        elif choice == "3":
            view_analytics(data)
        elif choice == "4":
            delete_url(data)
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()