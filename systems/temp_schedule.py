#1 ===========
"""
def celsius_to_fahrenheit():
    while True:
        temp_c = input("Enter temperature in Celsius: ").strip()
        if temp_c.replace('.', '', 1).isdigit() or (temp_c.startswith('-') and temp_c[1:].replace('.', '', 1).isdigit()):
            temp_c = float(temp_c)
            temp_f = (9/5) * temp_c + 32
            print(f"{temp_c}°C is {temp_f:.2f}°F")
            break
        else:
            print("Invalid input. Please enter a numeric temperature.")

celsius_to_fahrenheit()
"""
#2 ================
def get_weather_report(temperature, is_sunny):
    '''Generate a professional weather report based on temperature and sun conditions.'''

    # Validate input
    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number")
    # Determine temperature category with clear thresholds
    if temperature >= 30:
        temp_category = "HOT"
    elif temperature <= 0:
        temp_category = "COLD"
    else:
        temp_category = "WARM"

    # Determine sky condition
    sky_condition = "SUNNY" if is_sunny else "CLOUDY"

    # Generate comprehensive report
    return f"Weather Report: {temp_category} and {sky_condition}"
# Usage
temp = 35
is_sunny = False
weather_report = get_weather_report(temp, is_sunny)
print(weather_report)
# Output: "Weather Report: HOT and CLOUDY"

