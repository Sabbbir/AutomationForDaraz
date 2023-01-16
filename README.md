# AutomationForDaraz
## Description
This project is designed to automate the process of sorting undelivered products from Daraz. It takes in two input files: a large CSV file that has been downloaded from Daraz, and an Excel file that contains the customer IDs. The program sorts out the customer IDs from the CSV file and compares the inputs from the Excel file. It then gives the result of the undelivered customer IDs and the number of days that have passed since the order was placed.

The script reads the CSV file, extracts the customer IDs and the order dates, and matches them with the customer IDs in the Excel file. It then calculates the number of days that have passed since the order was placed and sorts the undelivered products based on the number of days passed. The result is then stored in a new excel sheet.

## Usage
- Run the script using command line
- Enter the files when prompted.
- The script will output the result in CSV format which can be opened using Excel.

## Requirements
- Python3
- Pandas library
- Arrow
- Tkinter
- OS module

## Notes
- Ensure that the customer IDs in the CSV file match the customer IDs in the Excel file
- You can get the CSV file from your seller ID
- The script expects one column of the Excel file to contain the customer IDs.
- The script is designed to handle large CSV files, so it may take some time to run depending on the size of the input file.

## Bug
- The Excel file only expects numerical value. And string will cause crashing the Script. So, as a result the program will neither give any output nor any prompt of the error message.
