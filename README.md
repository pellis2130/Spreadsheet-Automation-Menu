# Spreadsheet Automation - Weight Conversion

## Project Overview

This Python project is a Spreadsheet Automation program that allows a user to enter weight information and convert the entered values from pounds to kilograms.

The project demonstrates the use of functions, arguments, return values, loops, conditional statements, user input, and date/time functionality in Python.

## Features

- Displays a Spreadsheet Automation menu
- Allows the user to select the Input Data option
- Accepts multiple data entries from the user
- Uses a `for` loop to process the requested number of entries
- Accepts a date and weight for each entry
- Converts weight from pounds to kilograms
- Displays the original and converted values
- Displays the current date and time when information is processed
- Displays an error message for menu functionality that has not been implemented yet

## Menu Options

The program displays the following options:

1. Input Data
2. View Current Data
3. Generate Report

Currently, the **Input Data** option is implemented. The other options will be developed in future stages of the project.

## Weight Conversion

The program converts pounds to kilograms using the following formula:

`kilograms = pounds / 2.205`

For example:

`100 pounds = approximately 45.35 kilograms`

## Functions

### `convertData(data)`

Accepts a weight in pounds as an argument, converts the value to kilograms, and returns the converted value.

### `getInput()`

Asks the user how many entries will be entered. It then uses a `for` loop to collect a date and weight for each entry. The function calls `convertData()` and displays the original and converted information.

## Example Output

```text
priell10453's Spreadsheet Automation Menu
Choose a number from the following options
1 Input Data
2 View Current Data
3 Generate Report

Enter an option number: 1
You selected 1 at 2026-08-16 14:05:00

How many entries are you inputting? 3

Enter a date: 10/10/2026
Enter the weight in pounds for the inputted date: 80
The following was saved at 2026-08-16 14:05:15:
10/10/2026,80,36.281179138321995
