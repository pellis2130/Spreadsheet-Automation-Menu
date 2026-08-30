# Spreadsheet Automation Project

## Project Summary

This project is a Python-based spreadsheet automation program that allows users to enter, store, view, convert, and graph weight data.

The program collects weight measurements in pounds and automatically converts them to kilograms. The date, pounds, and converted kilograms are then stored in a CSV file.

The application includes a menu with three options:

1. Input Data
2. View Current Data
3. Generate Report

The Generate Report option allows the user to select either a line chart or bar chart. The user can also choose whether the chart displays the original weight in pounds or the converted weight in kilograms.

The program uses the openpyxl Python library to create an Excel spreadsheet named `final.xlsx`. The spreadsheet contains the weight data and the selected chart. The chart includes dates as the x-axis labels, the selected weight measurement as the y-axis, and a title containing the student ID and current date.

## Features

- Accepts weight data from the user
- Converts pounds to kilograms
- Saves information to a CSV file
- Displays previously saved data
- Generates Excel reports
- Creates bar charts
- Creates line charts
- Allows the user to graph pounds or kilograms
- Adds appropriate chart titles and axis labels

## Technologies Used

- Python
- CSV files
- openpyxl
- Microsoft Excel
- GitHub

## Files

- `SpreadsheetAutomationMenu.py` - Main Python program
- `ZooData.csv` - Stores the weight data
- `final.xlsx` - Generated Excel report and chart

## How to Run

1. Install Python.
2. Install openpyxl using:

   `pip install openpyxl`

3. Run `SpreadsheetAutomationMenu.py`.
4. Select an option from the main menu.
5. Select option `3` to generate an Excel report.
6. Choose a line or bar chart.
7. Choose pounds or kilograms as the data source.
8. Open `final.xlsx` to view the generated report and chart.

## Author

Princess Ellis
