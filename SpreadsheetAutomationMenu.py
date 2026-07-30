from datetime import datetime

print("priell10453 Spreadsheet Automation Menu")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called selected_option.
selected_option = input("Enter an option number: ")

print("Option", selected_option, "has been selected.")
print("The current date and time is", str(datetime.now()))
