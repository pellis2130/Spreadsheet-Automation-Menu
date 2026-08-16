# Name: Princess Ellis
# Date: August 16, 2026
# Description: This program displays a spreadsheet automation menu,
# accepts weight data, and converts pounds to kilograms.

from datetime import datetime

studentId = "priell10453"

menuOptions = (
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
)


def convertData(data):
    convertedValue = data / 2.205
    return convertedValue


def getInput():
    numberOfEntries = int(input("How many entries are you inputting? "))

    for entry in range(numberOfEntries):
        inputDate = input("Enter a date: ")
        weight = int(input("Enter the weight in pounds for the inputted date: "))

        # convertData requires the weight in pounds as an argument
        # and returns the converted weight in kilograms.
        convertedWeight = convertData(weight)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{inputDate},{weight},{convertedWeight}")


print(f"{studentId}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

for menuOption in menuOptions:
    print(menuOption)

selectedOption = input("Enter an option number: ")

if selectedOption == "1":
    print(f"You selected {selectedOption} at {datetime.now()}")
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
