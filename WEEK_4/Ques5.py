import re
common_passwords = {
    "123456", "password", "12345678", "qwerty", "abc123", "123456789", "111111", "123123", "admin", "letmein"
}

def pwd_strength(password):
    score = 0
    feedback = []

    if password.lower() in common_passwords:
        feedback.append("Too common Password")
        return "weak", feedback
    
    lenght = len(password)

    if lenght >= 12:
        feedback.append("Good Length")
        score+=3
    elif lenght >= 8:
        feedback.append("Moderate Length")
        score+=2
    elif lenght >= 6:
        feedback.append("Password is Short")
        score+=1
    else:
        feedback.append("Too Short")
        return "weak", feedback
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase.")
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains Uppercase.")
    if re.search(r"\d", password):
        score += 1
        feedback.append("Contains digits.")
    if re.search(r"\W", password):
        score += 1
        feedback.append("Contains Special Char.")

    if score <= 2:
        return "Weak", feedback
    elif score <= 4:
        return "Medium", feedback
    elif score <= 6:
        return "Strong", feedback
    else:
        return "Very Strong", feedback
    
pwd = input("Enter your password : ")
strength, comment = pwd_strength(pwd)
print(f"\nPassword: {pwd}\nStrength: {strength}")
for comment in comment:
    print(f" - {comment}")