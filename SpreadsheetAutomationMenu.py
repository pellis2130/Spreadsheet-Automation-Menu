# Name: Princess Ellis
# Date: August 23, 2026
# Description: This program displays a spreadsheet automation menu,
# accepts weight data, converts pounds to kilograms, and saves
# the information to a CSV file.

from datetime import datetime

studentId = "priell10453"
filePath = "ZooData.csv"

menuOptions = (
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
)


# This function converts a weight from pounds to kilograms.
def convertData(data):
    convertedValue = data / 2.205
    return convertedValue


# This function inserts comma-separated data into a CSV file.
def insertData(path, data):
    try:
        # Append permission allows writing without removing existing data.
        with open(path, "a") as file:
            file.write(data + "\n")
        return True

    except Exception as error:
        print(f"Error writing to the file: {error}")
        return False


# This function reads and displays the contents of a CSV file.
def viewData(path):
    try:
        # Read-only permission is the minimum permission needed.
        with open(path, "r") as file:
            print(f"\nReading data from: {path}")
            print("--------------------------------")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print(f"Error: {path} does not exist.")

    except Exception as error:
        print(f"Error reading the file: {error}")


# This function collects weight information and saves it to the CSV file.
def getInput():
    try:
        numberOfEntries = int(input("How many entries are you inputting? "))

        for entry in range(numberOfEntries):
            inputDate = input("Enter a date: ")
            weight = int(
                input("Enter the weight in pounds for the inputted date: ")
            )

            convertedWeight = convertData(weight)

            data = f"{inputDate},{weight},{convertedWeight:.2f}"

            if insertData(filePath, data):
                print(
                    f"The following data was saved at "
                    f"{datetime.now()}: {data}."
                )

    except ValueError:
        print("Error: Please enter a valid number.")

    except Exception as error:
        print(f"Error: {error}")


# This function displays the main application menu.
def displayMenu():
    print(f"{studentId}'s Spreadsheet Automation Menu")
    print("Choose a number from the following options")

    for menuOption in menuOptions:
        print(menuOption)


displayMenu()

selectedOption = input("Enter an option number: ")

if selectedOption == "1":
    print(f"You selected {selectedOption} at {datetime.now()}")
    getInput()

elif selectedOption == "2":
    print(f"You selected {selectedOption} at {datetime.now()}")
    viewData(filePath)

else:
    print("Error: The chosen functionality is not implemented yet")
