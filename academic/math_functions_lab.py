#1 =============
"""
import math
def demo_builtins():
    x, y, z = 4.75, -5, 7
    print("\n🔢 Built-in Functions:")
    print(f"round({x}) → {round(x)}")
    print(f"abs({y}) → {abs(y)}")
    print(f"pow(5,3) → {pow(5,3)}")
    print(f"max → {max(x,y,z)}, min → {min(x,y,z)}")

def demo_math_module():
    x = 9.9
    print("\n📐 Math Module:")
    print(f"π ≈ {math.pi:.4f}, e ≈ {math.e:.4f}")
    print(f"√{x} ≈ {math.sqrt(x):.4f}")
    print(f"ceil({x}) → {math.ceil(x)}, floor({x}) → {math.floor(x)}")

def calculate_circle_circumference():
    try:
        r = float(input("\nEnter circle radius: "))
        if r >= 0:
            c = 2 * math.pi * r
            print(f"✅ Circumference = {c:.2f} cm")
        else:
            print("⚠️ Radius can't be negative.")
    except ValueError:
        print("⚠️ Invalid number.")

def calculate_circle_area():
    try:
        r = float(input("\nEnter circle radius: "))
        if r >= 0:
            a = math.pi * r**2
            print(f"✅ Area = {a:.2f} cm²")
        else:
            print("⚠️ Radius can't be negative.")
    except ValueError:
        print("⚠️ Invalid number.")

def pythagorean_theorem():
    try:
        a = float(input("\nEnter side A: "))
        b = float(input("Enter side B: "))
        if a >= 0 and b >= 0:
            c = math.sqrt(a**2 + b**2)
            print(f"✅ Hypotenuse C = {c:.2f}")
        else:
            print("⚠️ Sides can't be negative.")
    except ValueError:
        print("⚠️ Invalid number.")

# ➡️ RUN DEMOS
if __name__ == "__main__":
    demo_builtins()
    demo_math_module()
    calculate_circle_circumference()
    calculate_circle_area()
    pythagorean_theorem()
"""
#2 ========================

"""
def simple_calculator():
    while True:
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
            break
        except ValueError:
            print("Please enter valid numbers.")

    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in ['+', '-', '*', '/']:
            if op == '/' and num2 == 0:
                print("Cannot divide by zero. Enter a non-zero second number.")
                num2 = float(input("Enter second number: ").strip())
                continue
            break
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    else:
        result = num1 / num2

    print(f"Result: {result}")
simple_calculator()
"""

#3 =============

def contact_book():
    contacts = {}

    while True:
        action = input("Choose action: add, search, quit: ").strip().lower()
        if action == "add":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            contacts[name] = phone
            print(f"Contact for {name} added.")
        elif action == "search":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"{name}'s phone number is {contacts[name]}")
            else:
                print(f"No contact found for {name}.")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose add, search, or quit.")

contact_book()