while True:
    # Step 1: Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))

    # Step 2: Convert height from cm to meters
    height_m = height_cm / 100

    # Step 3: Calculate BMI
    bmi = weight / (height_m ** 2)

    # Step 4: Determine fitness category based on BMI
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Step 5: Heart rate calculations
    max_heart_rate = 220 - age
    moderate_min = int(max_heart_rate * 0.50)
    moderate_max = int(max_heart_rate * 0.70)
    vigorous_min = int(max_heart_rate * 0.70)
    vigorous_max = int(max_heart_rate * 0.85)

    # Step 6: Display results
    print("\n--- Fitness Report ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height_cm} cm")
    print(f"BMI: {bmi:.2f}")
    print(f"Fitness Category: {category}")
    print(f"Max Heart Rate: {max_heart_rate} bpm")
    print(f"Target Heart Rate (Moderate Intensity): {moderate_min}-{moderate_max} bpm")
    print(f"Target Heart Rate (Vigorous Intensity): {vigorous_min}-{vigorous_max} bpm")

    # Step 7: Ask if the user wants to continue
    option = input("\nPlease enter 'c' to continue or 't' to terminate: ").lower()
    if option != 'c':
        print("Program terminated.")
        break