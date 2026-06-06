import random
import string

def generate_password(length=12):
    # Characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    strength = 0
    # Criteria checks
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 12:
        strength += 1
    
    # Strength levels
    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }
    return levels.get(strength, "Unknown")

# Example usage
new_password = generate_password(16)
print("Generated Password:", new_password)
print("Strength:", check_strength(new_password))
