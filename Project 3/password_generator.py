
import random
import string


# ============================================================
# Password Generator
# ============================================================

def generate_password(length):
    """
    Generate a random password of the specified length.

    The generated password contains at least:
    - One uppercase/lowercase letter
    - One number
    - One special character
    """

    letters = string.ascii_letters
    numbers = string.digits
    special_characters = "!@#$%^&*?"

    all_characters = letters + numbers + special_characters

    # Guarantee password complexity
    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Generate remaining characters
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    # Randomize character positions
    random.shuffle(password)

    # Convert list into a string
    return "".join(password)


# ============================================================
# Display Header
# ============================================================

def display_header():
    """Display the application header."""

    print("\n" + "=" * 55)
    print("          DECODELABS - PASSWORD GENERATOR")
    print("=" * 55)
    print("Generate strong random passwords with Python")
    print("=" * 55)


# ============================================================
# Main Program
# ============================================================

def main():
    """Run the password generator application."""

    display_header()

    while True:

        try:
            length = int(input("\nEnter password length: "))

            # Validate password length
            if length < 4:
                print("❌ Password length must be at least 4 characters.")
                continue

            # Generate password
            password = generate_password(length)

            print("\n" + "-" * 55)
            print("✅ Password generated successfully!")
            print("-" * 55)
            print(f"Password : {password}")
            print(f"Length   : {len(password)}")
            print("-" * 55)

            # Ask user whether to generate another password
            again = input(
                "\nGenerate another password? (y/n): "
            ).strip().lower()

            if again != "y":
                print("\n🔐 Thank you for using DecodeLabs Password Generator!")
                print("Program closed successfully.\n")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a numeric password length.")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()