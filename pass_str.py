import re

def assess_password_strength(password):
    score = 0
    criteria = {
        "Length >= 8": len(password) >= 8,
        "Contain lowercase": bool(re.search(r'[a-z]', password)),
        "Contain uppercase": bool(re.search(r'[A-Z]', password)),
        "Contains digit": bool(re.search(r'\d', password)),
        "Contain Special character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }
    print("Password Assessment:")
    for desc, passed in criteria.items():
        print(f"- {desc}: {'OK' if passed else 'NO'}")
        score += int(passed)
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    print(f"\nOverall Strength: {strength}")
password = input("Enter a password to assess: ")
assess_password_strength(password)
