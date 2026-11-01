import random

battery = 100.0

for step in range (1, 11):
    battery_drop = random.uniform(1.5, 3.5)
    battery -= battery_drop

    print(f"Waypoint {step}: Battery dropped by {battery_drop:.2f}%. Remaining battery: {battery:.2f}%")

    if battery < 80:
        print(f"[CAUTION] Batter is below 80%. Current battery: {battery:.2f}%")

    if battery < 75:
        print(f"[EMERGENCY RETURN TRIGGERED] Battery is below 75%. Current battery: {battery:.2f}%")
        break