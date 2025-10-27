#1 ==============
"""
def happy_birthday(name, age):
    if not isinstance(age, int) or age <= 0:
        return f"Error: Age for {name} must be a positive integer."
    year_word = "year" if age == 1 else "years"
    return (
        f"Happy birthday to {name}!\n"
        f"You are {age} {year_word} old!\n"
        "Happy birthday to you!\n"
    )

# Collect birthday info from the user
people = []
while True:
    name = input("Enter the name (or 'quit' to stop): ").strip()
    if name.lower() == 'quit':
        break
    age_input = input(f"Enter {name}'s age: ").strip()
    if not age_input.isdigit() or int(age_input) <= 0:
        print("Please enter a valid positive integer for age.")
        continue
    age = int(age_input)
    people.append((name, age))

# Generate and print birthday messages
messages = []
for name, age in people:
    message = happy_birthday(name, age)
    print(message)
    messages.append(message)

# Optionally, save messages to a file
save = input(
    "Would you like to save these messages to a file? (yes/no): "
).strip().lower()
if save in ("yes", "y"):
    filename = "birthday_messages.txt"
    with open(filename, "w") as file:
        for msg in messages:
            file.write(msg + "\n")
    print(f"Messages saved to {filename}.")

print("All done! Have a great day!")
"""

#2 ==============

def happy_birthday(name, age):
    """
    Generate a personalized birthday message.

    Args:
        name (str): The name of the birthday person
        age (int): The age of the birthday person (must be positive integer)

    Returns:
        str: Formatted birthday message or error message
    """
    if not isinstance(age, int) or age <= 0:
        return f"Error: Age for {name} must be a positive integer."

    year_word = "year" if age == 1 else "years"

    return (
        f"Happy birthday to {name}!\n"
        f"You are {age} {year_word} old!\n"
        "Happy birthday to you!\n"
    )


def main():
    """Main function to run the birthday message generator."""
    people = []

    print("=== Birthday Message Generator ===")
    print("Enter information for each person (type 'quit' to finish)\n")

    while True:
        try:
            name = input("Enter the name: ").strip()

            if not name:
                print("Name cannot be empty. Please try again.")
                continue

            if name.lower() == 'quit':
                break

            age_input = input(f"Enter {name}'s age: ").strip()

            if not age_input.isdigit() or int(age_input) <= 0:
                print("Please enter a valid positive integer for age.")
                continue

            age = int(age_input)
            people.append((name, age))

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

    if not people:
        print("No birthday information entered. Exiting.")
        return

    print("\n" + "=" * 40)
    print("Generating birthday messages...")
    print("=" * 40)

    messages = []
    for name, age in people:
        message = happy_birthday(name, age)
        print(message)
        messages.append(message)

    try:
        save = input("\nWould you like to save these messages to a file? (yes/no): ").strip().lower()
        if save in ("yes", "y"):
            filename = "birthday_messages.txt"

            # Check if file already exists to prevent accidental overwrite
            import os
            if os.path.exists(filename):
                overwrite = input(f"'{filename}' already exists. Overwrite? (yes/no): ").strip().lower()
                if overwrite not in ("yes", "y"):
                    filename = input("Enter a new filename: ").strip()

            with open(filename, "w") as file:
                for msg in messages:
                    file.write(msg + "\n")
            print(f"Messages saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving to file: {e}")

    print("\nAll done! Have a great day!")


if __name__ == "__main__":
    main()
