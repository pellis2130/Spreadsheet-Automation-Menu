# Name: Princess Ellis
# Date: August 9, 2026
# Description: This program displays a spreadsheet automation menu,
# validates the user's selection, and prints the current date and time.

from datetime import datetime

studentId = "priell10453"

menuOptions = (
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
)

print(f"{studentId} Spreadsheet Automation Menu")
print("Choose a number from the following options")

# menuOption represents each available option stored in the menuOptions tuple.
for menuOption in menuOptions:
    print(menuOption)

selectedOption = input("Enter an option number: ")

if selectedOption in ("1", "2", "3"):
    print(f"You selected {selectedOption} at {datetime.now()}")
else:
    print("Error: Invalid choice selected.")
