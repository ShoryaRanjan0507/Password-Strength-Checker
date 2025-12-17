def check_password_strength(password):
    score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "@#$%&!*"

    if len(password) >= 8:
        score += 1

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        strength = "WEAK"
    elif score == 3 or score == 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return strength, score, has_upper, has_lower, has_digit, has_special


password = input("Enter your password: ")

strength, score, has_upper, has_lower, has_digit, has_special = check_password_strength(password)

print("\nPassword Strength Analysis:")
print("Strength :", strength)
print("Score    :", score, "/ 5")

if score < 5:
    print("\nSuggestions to make it stronger:")
    if len(password) < 8:
        print("- Increase password length to at least 8 characters")
    if not has_upper:
        print("- Add at least one uppercase letter (A-Z)")
    if not has_lower:
        print("- Add at least one lowercase letter (a-z)")
    if not has_digit:
        print("- Add at least one digit (0-9)")
    if not has_special:
        print("- Add at least one special character (@ # $ % & ! *)")
