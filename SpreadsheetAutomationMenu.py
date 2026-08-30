# Name: Princess Ellis
# Date: August 30, 2026
# Description: This program displays a spreadsheet automation menu,
# accepts weight data, converts pounds to kilograms, saves the information
# to a CSV file, and generates a line or bar chart in an Excel spreadsheet.

from datetime import datetime
import csv
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference

studentId = "priell10453"
filePath = "ZooData.csv"

menuOptions = (
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
)


# This function converts a weight from pounds to kilograms.
# Argument: data (int or float)
# Return value: float containing the converted weight in kilograms.
def convertData(data):
    convertedValue = data / 2.205
    return convertedValue


# This function inserts comma-separated data into a CSV file.
# Arguments: path (str), data (str)
# Return value: True if the data is saved successfully; otherwise False.
def insertData(path, data):
    try:
        # Append permission allows writing without removing existing data.
        with open(path, "a", newline="") as file:
            file.write(data + "\n")
        return True

    except Exception as error:
        print(f"Error writing to the file: {error}")
        return False


# This function reads and displays the contents of a CSV file.
# Argument: path (str)
# Return value: None.
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
# Arguments: None.
# Return value: None.
def getInput():
    try:
        numberOfEntries = int(input("How many entries are you inputting? "))

        for entry in range(numberOfEntries):
            inputDate = input("Enter a date: ")
            weight = float(
                input("Enter the weight in pounds for the inputted date: ")
            )

            convertedWeight = convertData(weight)
            data = f"{inputDate},{weight:.2f},{convertedWeight:.2f}"

            if insertData(filePath, data):
                print(
                    f"The following data was saved at "
                    f"{datetime.now()}: {data}."
                )

    except ValueError:
        print("Error: Please enter a valid number.")

    except Exception as error:
        print(f"Error: {error}")


# This function creates an Excel chart from data in a CSV file.
# Arguments: path (str) - path to the CSV file; chartType (str) - "line" or "bar".
# Return value: None. The function creates and saves final.xlsx.
def createChart(path, chartType):
    try:
        print("\nChoose the data source to graph:")
        print("1 Pounds")
        print("2 Kilograms")
        dataChoice = input("Enter 1 or 2: ")

        if dataChoice == "1":
            selectedColumn = 2
            selectedHeading = "Pounds"
            yAxisTitle = "Weight (Pounds)"
        elif dataChoice == "2":
            selectedColumn = 3
            selectedHeading = "Kilograms"
            yAxisTitle = "Weight (Kilograms)"
        else:
            print("Error: Please choose 1 or 2.")
            return

        dates = []
        pounds = []
        kilograms = []

        with open(path, "r", newline="") as csvFile:
            reader = csv.reader(csvFile)

            for row in reader:
                if len(row) < 3:
                    continue

                try:
                    inputDate = row[0].strip()
                    poundValue = float(row[1])
                    kilogramValue = float(row[2])
                except ValueError:
                    # Skip any header or invalid row.
                    continue

                dates.append(inputDate)
                pounds.append(poundValue)
                kilograms.append(kilogramValue)

        if not dates:
            print("Error: There is no valid data in the CSV file.")
            return

        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Weight Report"

        worksheet.append(["Date", "Pounds", "Kilograms"])

        for index in range(len(dates)):
            worksheet.append([dates[index], pounds[index], kilograms[index]])

        if chartType.lower() == "bar":
            chart = BarChart()
            chart.style = 10
        elif chartType.lower() == "line":
            chart = LineChart()
            chart.style = 13
        else:
            print("Error: Invalid chart type.")
            return

        data = Reference(
            worksheet,
            min_col=selectedColumn,
            min_row=1,
            max_row=len(dates) + 1
        )
        categories = Reference(
            worksheet,
            min_col=1,
            min_row=2,
            max_row=len(dates) + 1
        )

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.title = f"{studentId} {datetime.now().strftime('%m/%d/%Y')}"
        chart.x_axis.title = "Date"
        chart.y_axis.title = yAxisTitle
        chart.height = 10
        chart.width = 18

        worksheet.add_chart(chart, "E2")

        worksheet.column_dimensions["A"].width = 16
        worksheet.column_dimensions["B"].width = 14
        worksheet.column_dimensions["C"].width = 14

        workbook.save("final.xlsx")

        print(
            f"\nA {chartType} chart using {selectedHeading.lower()} "
            "was created successfully."
        )
        print("The report was saved as final.xlsx")

    except FileNotFoundError:
        print(f"Error: {path} does not exist.")

    except Exception as error:
        print(f"Error creating chart: {error}")


# This function asks the user which graph type to create and calls createChart.
# Argument: path (str) - path to the CSV data file.
# Return value: None.
def generateReport(path):
    print("\nChoose the graph type:")
    print("1 Line Chart")
    print("2 Bar Chart")
    graphChoice = input("Enter 1 or 2: ")

    if graphChoice == "1":
        createChart(path, "line")
    elif graphChoice == "2":
        createChart(path, "bar")
    else:
        print("Error: Please choose 1 or 2.")


# This function displays the main application menu.
# Arguments: None.
# Return value: None.
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

elif selectedOption == "3":
    print(f"You selected {selectedOption} at {datetime.now()}")
    generateReport(filePath)

else:
    print("Error: Please choose option 1, 2, or 3.")
