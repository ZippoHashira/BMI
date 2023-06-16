# Ask the user's weight in 'kg' and height in 'm' and store them in float variables.
weight = float(input("Please enter you weight (kg): "))
height = float(input("Please enter your height (m): "))

# Use the BMI formula 'weight/(height * height)' to calculate the user's BMI and print it out.
BMI = weight / (height * height)
print(f"Your BMI is: {round(BMI, 1)}")

# Check and print "You are obese" if the user's BMI is 30 or greater.
if BMI >= 30:
    print("You're in obese range.")

# Check and print "You are overweight" if the user's BMI is 25 or greater.
elif BMI >= 25:
    print("You're in the overweight range.")

# Check and print "You are normal" if the user's BMI is 18.5 or greater.
elif BMI >= 18.5:
    print("You're in the healthy weight range.")

# If all the above conditions are false, meaning the user is less than 18.5, print "Print you are underweight".
else:
    print("You are in the underweight range.")
