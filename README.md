# Spreadsheet Automation - Graphing Dynamically Generated Data

## Project Summary
This Python project automates weight data entry, converts pounds to kilograms, stores the information in a CSV file, and generates an Excel report with a configurable line or bar chart.

## Features
- Input weight data by date
- Convert pounds to kilograms
- Save data to `ZooData.csv`
- View the current CSV data
- Generate either a line chart or bar chart
- Choose pounds or kilograms as the chart data source
- Save the report and chart to `final.xlsx`
- Add the student ID and current date as the chart title
- Label the chart axes appropriately

## Required Library
The project uses `openpyxl` for Excel spreadsheet and chart generation.

Install it with:

```bash
pip install openpyxl
```

## Run the Program

```bash
python SpreadsheetAutomationMenu.py
```

For the required screenshot, select:
1. `3` - Generate Report
2. `2` - Bar Chart (or `1` for Line Chart)
3. `2` - Kilograms (or `1` for Pounds)

The program creates `final.xlsx` in the same folder.

## Files
- `SpreadsheetAutomationMenu.py` - Main Python program
- `ZooData.csv` - Weight data
- `final.xlsx` - Excel report containing the chart

## Author
Princess Ellis
