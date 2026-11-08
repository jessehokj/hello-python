# Version 3: Enhanced Interactive Greeting
# Intro to AI - Week 3 Assignment

def main():
    print("Hello, World!")
    print("Welcome to my enhanced Python program.")

    name = input("What is your name? ").strip()

    while not name:
        print("Please enter a valid name.")
        name = input("What is your name? ").strip()

    print(f"\nNice to meet you, {name}!")

    print("\nChoose a greeting:")
    print("1. Friendly")
    print("2. Motivational")
    print("3. Professional")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print(f"Hey {name}! Hope you have an amazing day!")
    elif choice == "2":
        print(f"Keep learning, {name}! Every step counts!")
    elif choice == "3":
        print(f"Greetings, {name}. Wishing you a productive day.")
    else:
        print(f"Thank you for visiting, {name}!")

    print("\nThank you for trying my Python program.")

if __name__ == "__main__":
    main()
