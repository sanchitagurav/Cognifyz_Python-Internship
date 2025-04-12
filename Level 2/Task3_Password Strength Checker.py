import re

def check_password_strength(password):
    strength = "Weak"
    length_error = len(password) < 8
    upper_error = re.search(r'[A-Z]', password) is None
    lower_error = re.search(r'[a-z]', password) is None
    digit_error = re.search(r'\d', password) is None
    special_error = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None

    # Display which rules passed or failed
    print("\nPassword Check:")
    print(f"✔️ Minimum 8 characters: {'Passed' if not length_error else 'Failed'}")
    print(f"✔️ Uppercase letter: {'Passed' if not upper_error else 'Failed'}")
    print(f"✔️ Lowercase letter: {'Passed' if not lower_error else 'Failed'}")
    print(f"✔️ Number: {'Passed' if not digit_error else 'Failed'}")
    print(f"✔️ Special character: {'Passed' if not special_error else 'Failed'}")

    # Decide strength level
    if not (length_error or upper_error or lower_error or digit_error or special_error):
        strength = "Strong"
    elif not (length_error or (upper_error and lower_error)):
        strength = "Medium"

    return f"\n🔐 Password Strength: {strength}"

# Example usage
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
