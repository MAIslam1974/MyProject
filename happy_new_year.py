#1 =================
"""
import time

print("Countdown to New Year starts now!")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("HAPPY NEW YEAR!")
"""
#2 ==================
"""
import time
def countdown(seconds=10):
    print("🎆 Countdown to New Year starts now! 🎆\n")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end="\r", flush=True)
        time.sleep(1)
    print("✨🎉 HAPPY NEW YEAR! 🎉✨")

if __name__ == "__main__":
    countdown()
"""
#3 ====================

import time
import sys
def countdown(seconds: int = 10) -> None:
# Display a countdown timer and celebrate the New Year.
    print("🎆 Countdown to the New Year starts now! 🎆\n")
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{i:2d} seconds remaining...")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r🎉 HAPPY NEW YEAR! 🎉            \n")

if __name__ == "__main__":
    countdown(10)


