import random
import string

#  List of common passwords
common_passwords = [
    "123456", "password", "123456789", "qwerty", "abc123", "111111", 
    "123123", "password123", "admin", "letmein", "welcome", "monkey", 
    "1234567890", "iloveyou", "12345678", "admin123"
]

# Function to check the strength of a password
def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
     # Check if password is a common password
    if password.lower() in common_passwords:
        return " Weak (common password)"
    # Check for too short password
    if length < 6:
        return " Weak (too short)"
     # Strong password: long enough and contains all character types
    if length >= 8 and has_lower and has_upper and has_digit and has_special:
        return " Strong"
     # Medium password: at least 6 characters
    if length >= 6:
        return " Medium"
    return " Weak"

# Function to generate a secure random password
def generate_password(length=12):
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

#  Function to estimate the time to crack a password
def crack_time_estimate(password):
    # Determine charset size based on types of characters used
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    
    if charset_size == 0:
        return "Unable to calculate"
    
    combinations = charset_size ** len(password)
    guesses_per_second = 1_000_000_000  # 1 billion guesses per second (modern GPU)
    seconds = combinations / guesses_per_second
    
    if seconds < 1:
        return " Less than 1 second"
    elif seconds < 60:
        return f" {seconds:.2f} seconds"
    elif seconds < 3600:
        return f" {seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f" {seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.0f} days"
    elif seconds < 31536000 * 100:
        return f"{seconds/31536000:.1f} years"
    else:
        return f" {seconds/31536000:.0e} years"

# Main program
def main():
    while True:
        print("\n" + "="*50)
        print(" Password Strength Checker & Generator ")
        print("="*50)
        
        print("\nChoose an option:")
        print("1. Check a password")
        print("2. Generate a password")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            password = input("\nEnter your password: ")
            if not password:
                print(" Password cannot be empty!")
                continue
            
            strength = check_strength(password)
            time_to_crack = crack_time_estimate(password)
            
            print("\n" + "-"*50)
            print(f"Password Strength: {strength}")
            print(f"Estimated time to crack: {time_to_crack}")
            print("-"*50)
            
        elif choice == "2":
            try:
                length_input = input("\nEnter desired password length (default 12): ")
                length = int(length_input) if length_input else 12
                
                if length < 6:
                    print(" Minimum length is 6. Using 6 instead.")
                    length = 6
                
                password = generate_password(length)
                strength = check_strength(password)
                time_to_crack = crack_time_estimate(password)
                
                print("\n" + "-"*50)
                print(f" Generated password: {password}")
                print(f"Password Strength: {strength}")
                print(f"Estimated time to crack: {time_to_crack}")
                print("-"*50)
                
            except ValueError:
                print(" Please enter a valid number!")
                
        elif choice == "3":
            print("\n" + "="*50)
            print(" Stay secure! Thanks for using our tool!")
            print("="*50 + "\n")
            break
            
        else:
            print(" Invalid choice! Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()