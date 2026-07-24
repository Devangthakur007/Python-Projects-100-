def analyze_text(text: str) -> dict:
    # Character count including spaces
    char_count_with_spaces = len(text)
    
    # Character count excluding spaces
    char_count_no_spaces = len(text.replace(" ", ""))
    
    # Word count: splitting by default handles multiple spaces, tabs, and newlines
    words = text.split()
    word_count = len(words)
    
    return {
        "words": word_count,
        "chars_with_spaces": char_count_with_spaces,
        "chars_no_spaces": char_count_no_spaces
    }

# Example Usage
sample_text = """Python makes text analysis clean and efficient!
This is a multi-line string example."""

results = analyze_text(sample_text)

print(f"Words: {results['words']}")
print(f"Characters (with spaces): {results['chars_with_spaces']}")
print(f"Characters (without spaces): {results['chars_no_spaces']}")