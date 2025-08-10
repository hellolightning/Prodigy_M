import re

def password_strength(password):
    score = 0

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1

    # Criteria 2: Presence of uppercase and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1

    # Criteria 3: Presence of numbers
    if re.search(r"\d", password):
        score += 1

    # Criteria 4: Presence of special characters
    if re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/\\|`~]", password):
        score += 1

    return score

def feedback(score):
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score == 4:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    score = password_strength(password)
    strength = feedback(score)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()