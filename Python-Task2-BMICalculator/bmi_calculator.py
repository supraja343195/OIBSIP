def calculate_bmi():
    print("=== BMI Calculator ===")

    # Get weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))

            if weight <= 0:
                print("Error: Weight must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number for weight.")

    # Get height
    while True:
        try:
            height = float(input("Enter your height in meters (m): "))

            if height <= 0:
                print("Error: Height must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number for height.")

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Display result
    print("\n=== Result ===")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    calculate_bmi()