# Spreadsheet Automation - Weight Conversion and CSV File Handling

## Project Overview

This Python project is a Spreadsheet Automation program that allows a user to enter weight information, convert weight from pounds to kilograms, and save the information to a CSV file named `ZooData.csv`.

The project demonstrates the use of functions, arguments, return values, loops, conditional statements, exception handling, file operations, user input, and date/time functionality in Python.

## Features

* Displays a Spreadsheet Automation menu
* Allows the user to input weight data
* Accepts multiple entries from the user
* Uses a `for` loop to process the requested number of entries
* Accepts a date and weight for each entry
* Converts weight from pounds to kilograms
* Saves entered and converted data to `ZooData.csv`
* Creates `ZooData.csv` automatically if it does not already exist
* Appends new information without deleting existing data
* Allows the user to view previously saved CSV data
* Displays the path of the CSV file when reading data
* Uses `try-except` statements for error handling
* Displays the current date and time when information is saved
* Uses appropriate file permissions for reading and writing

## Menu Options

The program displays the following options:

1. Input Data
2. View Current Data
3. Generate Report

**Input Data** allows the user to enter information and save it to `ZooData.csv`.

**View Current Data** reads and displays the information currently stored in `ZooData.csv`.

**Generate Report** has not been implemented yet and will be developed in a future stage of the project.

## Weight Conversion

The program converts pounds to kilograms using the following formula:

`kilograms = pounds / 2.205`

For example:

`100 pounds = approximately 45.35 kilograms`

## Functions

### `convertData(data)`

Accepts a weight in pounds as an argument, converts the value to kilograms, and returns the converted value.

### `insertData(path, data)`

Accepts two arguments: the path to the CSV file and the comma-separated data that will be saved. The function opens the file in append mode so new information can be added without deleting existing information. A `try-except` statement handles errors that may occur while writing to the file.

### `viewData(path)`

Accepts the path to the CSV file as an argument. The function opens the file using read-only permissions and displays the file path and saved contents. A `try-except` statement handles missing files and other reading errors.

### `getInput()`

Asks the user how many entries they want to enter. It uses a `for` loop to collect a date and weight for each entry. The function calls `convertData()` to convert the weight and `insertData()` to save the information to `ZooData.csv`.

### `displayMenu()`

Displays the Spreadsheet Automation menu and the available options to the user.

## CSV File

The program uses a file named:

`ZooData.csv`

Each entry contains:

`Date, Weight in Pounds, Weight in Kilograms`

Example:

```text
8/20/2026,250,113.38
8/21/2026,248,112.47
8/22/2026,247,112.02
```

## Example - Input Data

```text
priell10453's Spreadsheet Automation Menu
Choose a number from the following options
1 Input Data
2 View Current Data
3 Generate Report

Enter an option number: 1
You selected 1 at 2026-08-23 15:30:00

How many entries are you inputting? 3

Enter a date: 8/20/2026
Enter the weight in pounds for the inputted date: 250
The following data was saved at 2026-08-23 15:30:10: 8/20/2026,250,113.38.

Enter a date: 8/21/2026
Enter the weight in pounds for the inputted date: 248
The following data was saved at 2026-08-23 15:30:20: 8/21/2026,248,112.47.

Enter a date: 8/22/2026
Enter the weight in pounds for the inputted date: 247
The following data was saved at 2026-08-23 15:30:30: 8/22/2026,247,112.02.
```

## Example - View Current Data

When the program is run again and option `2` is selected:

```text
priell10453's Spreadsheet Automation Menu
Choose a number from the following options
1 Input Data
2 View Current Data
3 Generate Report

Enter an option number: 2
You selected 2 at 2026-08-23 15:32:00

Reading data from: ZooData.csv
--------------------------------
8/20/2026,250,113.38
8/21/2026,248,112.47
8/22/2026,247,112.02
```

## Error Handling

The program uses `try-except` statements to handle potential errors when entering information, writing to the CSV file, and reading from the CSV file. If `ZooData.csv` does not exist when the user attempts to view it, the program displays an error message instead of crashing.
