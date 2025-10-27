
# 1=============
"""
'''
Ticket Price Calculator
Author: Aminul Islam
Version: 2.0
Description:
    A clean, professional program that calculates
    ticket prices based on age and ticket availability.
'''

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("❌ Invalid input. Please enter a valid number.")
    exit()

has_ticket = True  # Change to False for testing
base_price = 10.00
ticket_price = 0

# --- Age-based logic ---
if age < 0:
    print("You haven't been born yet.")
elif age == 0:
    print("You have just been born.")
elif age < 18:
    ticket_price = base_price * 0.5
    print("You are a child.")
    print(f"The ticket price for a child is ${ticket_price:.2f}")
elif age < 65:
    ticket_price = base_price
    print("You are an adult.")
    print(f"The ticket price for an adult is ${ticket_price:.2f}")
else:
    ticket_price = base_price * 0.75
    print("You are a senior citizen.")
    print(f"The ticket price for a senior citizen is ${ticket_price:.2f}")

# --- Ticket check ---
if age > 0:  # Only check ticket if age is positive
    if has_ticket:
        print("You may enter, You have a ticket.")
    else:
        print("You need to buy a ticket.")
"""

# 2==============
"""
def get_ticket_info():
# set age and ticket status from user  # type: ignore # type: ignore
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number for age.")
        return None, None

    has_ticket_input = input("Do you have a ticket? (yes/no): ").lower().strip()
    has_ticket = has_ticket_input in ['yes', 'y', 'true', '1']

    return age, has_ticket

def calculate_ticket_price(age, base_price=10.00):
   #Calculate ticket price based on age
    if age >= 65:
        category = "senior citizen"
        price = base_price * 0.75
    elif age >= 18:
        category = "adult"
        price = base_price
    else:
        category = "child"
        price = base_price * 0.5
    return category, price

def main():
    BASE_PRICE = 10.00

    # Get user input
    age, has_ticket = get_ticket_info()

    if age is None:  # Invalid input case
        return

    # Validate age first
    if age < 0:
        print("You haven't been born yet")
        return
    elif age == 0:
        print("You have just been born")
        return

    # Calculate price and display information
    category, price = calculate_ticket_price(age, BASE_PRICE)

    print(f"\n--- Ticket Information ---")
    print(f"You are a {category}")
    print(f"The ticket price for a {category} is ${price:.2f}")

    # Ticket verification
    if has_ticket:
        print("You may enter the venue.")
    else:
        print(f"You need to purchase a ticket for ${price:.2f}")

    # Additional information
    if age < 18:
        print("Note: Children must be accompanied by an adult.")

# Run the program
if __name__ == "__main__":
    main()
"""
# 3============

def get_ticket_info() -> tuple[int | None, bool | None]:
    '''
    Prompt the user for their age and ticket possession status.

    Returns:
        tuple: (age, has_ticket)
               - age (int or None): The user's age if valid, otherwise None.
               - has_ticket (bool or None): Whether the user has a ticket.
    '''
    try:
        age = int(input("Enter your age: ").strip())
        if age < 0:
            print("Invalid input: Age cannot be negative.")
            return None, None
    except ValueError:
        print("Invalid input: Please enter a valid number for age.")
        return None, None

    has_ticket_input = input("Do you have a ticket? (yes/no): ").strip().lower()
    has_ticket = has_ticket_input in {"yes", "y", "true", "1"}

    return age, has_ticket


def calculate_ticket_price(age: int, base_price: float = 10.00) -> tuple[str, float]:
    '''
    Calculate the ticket price based on the user's age.

    Args:
        age (int): The user's age.
        base_price (float): The standard ticket price.

    Returns:
        tuple: (category, price)
    '''
    if age >= 65:
        return "senior citizen", base_price * 0.75
    elif age >= 18:
        return "adult", base_price
    else:
        return "child", base_price * 0.5


def main() -> None:

# Main program to handle user interaction and ticket calculation.

    BASE_PRICE = 10.00
    age, has_ticket = get_ticket_info()

    if age is None:
        return  # Stop if invalid input

    # Special messages for age-specific edge cases
    if age == 0:
        print("You have just been born! No ticket required.")
        return
    elif age < 1:
        print("Invalid age entered.")
        return

    # Calculate price and display information
    category, price = calculate_ticket_price(age, BASE_PRICE)

    print("\n--- Ticket Information ---")
    print(f"Category       : {category.capitalize()}")
    print(f"Ticket Price   : ${price:.2f}")

    if has_ticket:
        print("Status         : You may enter the venue. Enjoy!")
    else:
        print(f"Status         : You need to purchase a ticket for ${price:.2f}")

    # Additional note for children
    if category == "child":
        print("Note           : Children must be accompanied by an adult.")

    print("\n✅ End of program execution.")


if __name__ == "__main__":
    main()

