def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


if __name__ == "__main__":
    print(capitalize_words("hello first year"))
    print(capitalize_words("a  b"))
