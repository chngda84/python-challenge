#PYTHON HW #1 - Pybank

# Import csv to read
import os
import csv

# define paths
cwd=os.getcwd()
print(cwd)

Pybankpath = os.path.join(cwd,"Resources","budget_data.csv")
Pybankoutput = os.path.join(cwd,"analysis","budget_analysis.txt")

# Lists to store data
MoM_Change_List =[]
MoM_ChangeMonth_List =[]

# Read csvfile
with open(Pybankpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    print(csvreader)

    # Store header row
    csvheader = next(csvreader)

    # Assign the first row profitloss numbers as the initial value
    row1 = next(csvreader)
    Total_Months = 1
    Total_ProfitLoss = int(row1[1])
    LastMonth_ProfitLoss = int(row1[1])
    Greatest_inc = int(row1[1])
    Greatest_dec = int(row1[1])
    Month_Greatest_inc=row1[0]
    Month_Greatest_dec=row1[0]

    for row in csvreader:
        
        #The total number of months included in the dataset
        Total_Months += 1

        # The net total amount of "Profit/Losses" over the entire period 
        Total_ProfitLoss += int(row[1])
        
        #The average of the changes in "Profit/Losses" over the entire period
        #Determine month on month change
        MoM_Change = int(row[1]) - LastMonth_ProfitLoss
        LastMonth_ProfitLoss =  int(row[1])
        MoM_Change_List.append(MoM_Change) 
        MoM_ChangeMonth_List.append(row[0])
        
        #The greatest increase in profits (date and amount) over the entire period
        if MoM_Change > Greatest_inc:
            Greatest_inc = MoM_Change
            Month_Greatest_inc = row[0]

        #The greatest decrease in losses (date and amount) over the entire period
        if MoM_Change < Greatest_dec:
            Greatest_dec = MoM_Change
            Month_Greatest_dec = row[0]

# Calculate average change
Average_change = round(sum(MoM_Change_List)/len(MoM_Change_List),2)

# Summarise output 
summary = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {Total_Months}\n"
   f"Total: ${Total_ProfitLoss}\n"
   f"Average  Change: ${Average_change}\n"
   f"Greatest Increase in Profits: {Month_Greatest_inc} (${Greatest_inc})\n"
   f"Greatest Decrease in Profits: {Month_Greatest_dec} (${Greatest_dec})\n")

# output to terminal
print(summary)
    
# output to txt
with open(Pybankoutput, 'w') as txtfile:
    txtfile.write(summary)