def is_palindrome(text):
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

# Example usage:
words = ["madam", "racecar", "hello", "A man a plan a canal Panama"]

for word in words:
    result = "Palindrome" if is_palindrome(word) else "Not a palindrome"
    print(f"'{word}' ➜ {result}")
