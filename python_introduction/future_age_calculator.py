# Instructions:
# Prompt the user to input their current age with the question: “How old are you? ”.
# Assume the user will input a valid integer value.
# Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
# Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
age = int(input("How old are you? "))
age_2050 = (2050 - 2025) + age

print(f"In 2050, you will be {age_2050} years old.")