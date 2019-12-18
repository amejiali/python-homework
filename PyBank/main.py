# PyBank - Python Homework - Andres Mejia - Rice FinTech Boot Camp - December 21, 2019
# Import the needed libraries to interact with csv files
## Path and csv

"""
This script processes an input file located in one level up running directory "../budget_data.csv".
After processing the data, prints the results on screen.
Also generated the file "../Financial_Analysis_PyBank.txt" located in the same directoy as input file. 
"""

# Import the needed libraries
## pathlib, statistics and csv

from statistics import mean
from pathlib import Path
import csv

# Defining Files Paths and names

file_path = Path('../budget_data.csv')             # Input File is in one level up directory
file_path_resutl = Path('../Financial_Analysis_PyBank.txt') # Output File is in one level up directory

# Initializing variables
my_file = ""           # to handle file in code
each_line = ""         # File line data
file_header = ""       # File Header
date_profit = {}       # date_profit --> dict with all the data from csv file
n_months = 0           # n_monts is the number of months in the csv file
net_pl = 0             # net_pl is the total amount of profit/losses
avg_ch_pl = 0          # avg_ch_pl --> average of changes in p&l
pl_ant = 0             # previous P&L
pl_curr = 0            # current P&L
delta_pl = {}          # changes in P&L by date


# Opening and Reading the file budget.csv from one level up directory

with open(file_path, 'r') as my_file:
    each_line = csv.reader (my_file, delimiter=',')
    file_header = next(each_line)
    for row in each_line:                              # Loop reading each line in file
        pl_curr = int(row[1])                          # Current P&L
        if pl_ant != 0:                                # Starts calculating sum_ch_pl from 2nd date
            delta_pl.update({row[0]:pl_curr - pl_ant}) # Storing the changes in P&L
        date_profit.update({row[0]:row[1]})            # Populating date_profit dictionary
        net_pl = net_pl + int(row[1])                  # Storing P&L
        pl_ant = int(row[1])                           # storing previous P&L for nrxt iteration
    n_months = len(date_profit)                        # n_months is the number of entries in dictionary 

print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months...................: {n_months}")
print(f"Total P&L......................: ${net_pl}")
print(f"Average Change.................: ${round(mean([int(i) for i in delta_pl.values()]),2)}")
print(f"Greatest Increase in Profits...: ${max([i for i in delta_pl.values()])}")
print(f"Greatest Decrease in Profits...: ${min([i for i in delta_pl.values()])}")

# Creating the result file "Financial_Analysis_PyBank.txt" in one level up directory.

with open(file_path_resutl, 'w') as my_file:
    my_file.write("Financial Analysis\n")
    my_file.write("------------------------------------------\n")
    my_file.write(f"Total Months...................: {n_months}\n")
    my_file.write(f"Total P&L......................: ${net_pl}\n")
    my_file.write(f"Average Change.................: ${round(mean([int(i) for i in delta_pl.values()]),2)}\n")
    my_file.write(f"Greatest Increase in Profits...: ${max([i for i in delta_pl.values()])}\n")
    my_file.write(f"Greatest Decrease in Profits...: ${min([i for i in delta_pl.values()])}")