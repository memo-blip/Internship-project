import re

def check_password_strength(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Make it at least 8 characters long.")
        return "Weak", feedback

    # Check for weak patterns
    only_letters = re.fullmatch(r"[a-zA-Z]+", password)
    only_numbers = re.fullmatch(r"\d+", password)
    letters_numbers = re.fullmatch(r"[a-zA-Z0-9]+", password)

    if only_letters or only_numbers or letters_numbers:
        feedback.append("Avoid using only letters or only numbers.")
        feedback.append("Include uppercase, lowercase, digits, and special characters.")
        return "Weak", feedback

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    special_chars = re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)
    special_count = len(special_chars)

    if has_upper and has_lower and has_digit:
        if special_count == 1:
            feedback.append("Add another special character to make it strong.")
            return "Moderate", feedback
        elif special_count > 1:
            return "Strong", []
        else:
            feedback.append("Add at least one special character.")
            return "Weak", feedback
    else:
        if not has_upper:
            feedback.append("Add at least one uppercase letter.")
        if not has_lower:
            feedback.append("Add at least one lowercase letter.")
        if not has_digit:
            feedback.append("Include at least one number.")
        if special_count == 0:
            feedback.append("Add special characters.")
        return "Weak", feedback

# Example usage
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)
print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for tip in suggestions:
        print(f" - {tip}")
