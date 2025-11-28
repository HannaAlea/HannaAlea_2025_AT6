from UserInputValidator import UserInputValidator


validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Sample input lists
inputs1 = ["5", "25", "-3", "uigh", "10"]
inputs2 = ["9", ".5", "0", "*Annyeong", "-9"]

result1 = validator1.validate_positive_integers(inputs1)
result2 = validator2.validate_positive_integers(inputs2)

# Print the results
print("Validator 1 valid integers:", result1)
print("Validator 2 valid integers:", result2)
