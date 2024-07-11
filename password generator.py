import random
import string

def generate_passwords(num_passwords):
    passwords = []

    print("Minimum length of password should be 3")
    for i in range(1, num_passwords + 1):
        while True:
            try:
                length = int(input(f"Enter the length of Password #{i}: "))
                if length < 3:
                    print("Password length is too short. Please enter a minimum of 3.")
                else:
                    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                    passwords.append(password)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return passwords

# Example usage:
if __name__ == "__main__":
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        
        passwords = generate_passwords(num_passwords)
        
        print(f"Generated Passwords: {passwords}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
