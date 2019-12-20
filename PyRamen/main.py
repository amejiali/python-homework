# PyRamen - Python Homework - Andres Mejia - Rice FinTech Boot Camp - December 21, 2019

"""
PyRamen Homework
This script processes an input file located in one level down of running directory "../Resources/budget_data.csv".
After processing the data, prints the results on a text file "./Resources/report.txt". 
"""

# @TODO: Import libraries
import csv
from pathlib import Path

my_file = ""           # to handle file in code
each_line = ""         # File line data
file_header = ""       # File Header


# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as my_file:
    each_line = csv.reader (my_file, delimiter=',')
    file_header = next(each_line)
    #print (f"{file_header}  Menu_file_header")
    for row in each_line:                               # Loop reading each line in file
        menu.append(row)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as my_file:
    each_line = csv.reader (my_file, delimiter=',')
    file_header = next(each_line)
    #print (f"{file_header}  Sales_file_header")
    for row in each_line:                               # Loop reading each line in file
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales & menu data variables
    Quantity = int(sale[3])
    Menu_Item = sale[4]
    Revenue = 0
    Cogs = 0
    Profit = 0
    Found = False
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for Item in menu:
        if Item[0] == Menu_Item:
            Revenue = int(Item[3]) * Quantity
            Cogs = int(Item[4]) * Quantity
            Profit = Revenue - Cogs
            Found = True
            break
        else:
            continue
        
    if Found:    
        # @TODO:
        # If the item value not in the report, add it as a new entry with initialized metrics
        # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
        if Menu_Item in report:
            # @TODO: Cumulatively add up the metrics for each item key
            Quantity += int(report[Menu_Item]["01-count"])
            Revenue += int(report[Menu_Item]["02-revenue"])
            Cogs += int(report[Menu_Item]["03-cogs"])
            Profit += int(report[Menu_Item]["04-profit"])
            report.update({Menu_Item:{"01-count":Quantity,"02-revenue":Revenue,"03-cogs":Cogs,"04-profit":Profit}})
        else:
            report.update({Menu_Item:{"01-count":Quantity,"02-revenue":Revenue,"03-cogs":Cogs,"04-profit":Profit}})
    else:
        print (f"************Item {Menu_Item} not in Menu. NO MATCH!!!***************")
    row_count += 1

file_path_resutl = Path('Resources/report.txt') # Output File is in one level up directory

# @TODO: Write out report to a text file (won't appear on the command line output)
with open(file_path_resutl, 'w') as my_file:
    my_file.write(str(report))
    
# @TODO: Print total number of records in sales data
print ("------------------------------------------------------------")
print (f"Total number of records in sales data file: {row_count}")
print ("------------------------------------------------------------")