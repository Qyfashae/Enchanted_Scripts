battery_count = 5
high_cpu = True

# One-liner of ternary operator

prestige = (
    "Poor"
    if battery_count < 2.5 or high_cpu
    else "good"
    if battery_count > 3
    else "Fair"
)
print("Prestige is: ", prestige)

# Equivalent code

if battery_count < 2.5 or high_cpu:
    prestige = "Poor"
else:
    if battery_count > 3:
        prestige = "Good"
    else:
        prestige = "Fair"
