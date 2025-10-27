#1 ========
"""
light = "green"  # Change this value to test different conditions

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Look and wait to go")
elif light == "green":
    print("Go")
else:
    print("Run! It's unsafe to wait.")

print("End of code")
"""
#2 ================
"""
def traffic_light_signal():
    light = input("Enter the traffic light color (red, yellow, green): ").strip().lower()

    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Look and wait to go")
    elif light == "green":
        print("Go")
    else:
        print("Invalid input or unsafe! Please be cautious.")

    print("End of code")

# Call the function to run
traffic_light_signal()
"""

#3 ==============
def traffic_light_signal(light=None):
    """
    Display action based on the traffic light color.

    Parameters:
        light (str, optional): The color of the traffic light.
                               If not provided, user input will be requested.
    """

    # Ask for input if not provided
    if light is None:
        light = input("Enter the traffic light color (red, yellow, green): ").strip().lower()
    else:
        light = light.strip().lower()

    # Dictionary-based mapping for cleaner logic
    actions = {
        "red": "Stop — vehicles must halt immediately.",
        "yellow": "Caution — prepare to stop or proceed carefully.",
        "green": "Go — you may proceed safely."
    }

    # Output based on user input
    action = actions.get(light, "Invalid color or unsafe input! Please check again.")
    print(action)
    print("End of code execution.")


# Example Calls
traffic_light_signal()            # Interactive mode
# traffic_light_signal("green")   # Direct test mode