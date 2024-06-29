#add import
import question_c
# Ask the user for the actual value of the property
val1 = float(input("Enter the actual value of the property: "))

# Calculate the assessment value
val2 = question_c.get_assessment_value(val1)

# Calculate the property tax
tax = question_c.get_tax_assessed(val2)

# Display the results
print(f"The assessment value of the property is: ${val2:.2f}")
print(f"The property tax is: ${tax:.2f}")

