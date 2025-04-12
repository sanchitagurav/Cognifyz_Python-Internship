import re

def is_valid_email(email):
    # Simple regex pattern for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# Example usage:
emails = ["example@gmail.com", "invalid-email@", "@domain.com", "name@site", "user@domain.co.in"]

for e in emails:
    print(f"{e} ➜ {'Valid' if is_valid_email(e) else 'Invalid'}")
