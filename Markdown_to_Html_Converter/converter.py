import re
import sys

def markdown_to_html(md_text: str) -> str:
    html = md_text

    html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"__(.*?)__", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", html)
    html = re.sub(r"_(.*?)_", r"<em>\1</em>", html)

    html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', html)
    html = re.sub(r"`(.*?)`", r"<code>\1</code>", html)

    lines = html.split("\n")
    processed_lines = []
    in_list = False

    for line in lines:
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            if not in_list:
                processed_lines.append("<ul>")
                in_list = True
            content = line.strip()[2:]
            processed_lines.append(f"  <li>{content}</li>")
        else:
            if in_list:
                processed_lines.append("</ul>")
                in_list = False
            
            trimmed = line.strip()
            if trimmed and not trimmed.startswith("<h") and not trimmed.startswith("</h"):
                processed_lines.append(f"<p>{trimmed}</p>")
            elif trimmed:
                processed_lines.append(trimmed)

    if in_list:
        processed_lines.append("</ul>")

    return "\n".join(processed_lines)

def convert_file(input_file: str, output_file: str):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_output = markdown_to_html(md_content)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_output)

        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except OSError as e:
        print(f"File error: {e}")

def main():
    print("=== Markdown to HTML Converter ===")
    print("1. Convert Markdown Text (Interactive)")
    print("2. Convert .md File to .html")
    print("3. Exit")

    choice = input("\nChoose an option (1-3): ").strip()

    if choice == "1":
        print("\nEnter Markdown text (press Enter twice or type END on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        
        md_text = "\n".join(lines)
        print("\n--- Converted HTML ---")
        print(markdown_to_html(md_text))

    elif choice == "2":
        in_file = input("Enter input Markdown file path (e.g., input.md): ").strip()
        out_file = input("Enter output HTML file path (e.g., output.html): ").strip()
        convert_file(in_file, out_file)

    elif choice == "3":
        print("Goodbye!")
        sys.exit()

if __name__ == "__main__":
    main()