# Get user input

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

# Check eligibility using nested if

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to insufficient weight.")
else:
    print("You are not eligible to donate blood as you are under 18.")
