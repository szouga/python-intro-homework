import os
import csv
from datetime import datetime

#number one
script_dir = os.path.dirname(os.path.abspath(__file__))
#^entire directory pathway
print(script_dir)

#have to go up one level (week-7) to find data folder, expenses file location and extract the data
parent_path = os.path.abspath(os.path.join(script_dir, ".."))

#create directory to data folder
data_path = os.path.abspath(os.path.join(parent_path, "data"))

if os.path.exists(data_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#number two
expenses_path = os.path.abspath(os.path.join(data_path, "expenses.csv"))
#print(expenses_path)

food_report_path = os.path.abspath(os.path.join(data_path, "food_report.txt"))

food_final_total = 0
food_amount_dictionary = {}

with open(expenses_path, 'r') as file:
    reader = csv.DictReader(file)
    food_amounts = []
    
    total = 0
    for row in reader:
        #number three
        amount = float(row['amount'])
        #number four
        if row['category'] == "Food":
            print(row['date'], row['category'], row['description'], amount)
            food_amounts.append(amount)
            food_amount_dictionary[row['date']]= amount
    #number five
    for amount in food_amounts:
        total += amount
    
    
    print(f"Total amount spent on food: ${total}")
    food_final_total = total
    
    
#with open automatically closes last file

now = datetime.now()
current_date = now.strftime("%B %d, %Y")
# with open(food_report_path, 'w') as report_file:
#     #Food Expense Report — generated [today's date as "Month DD, YYYY"]
#     writer = csv.DictWriter(report_file, fieldnames=['date', 'amount'])
#     report_file.write(f"Food Expense Report - generated {current_date}")
#     writer.writerows(food_amount_dictionary)

food_report = open(food_report_path, 'w')
food_report.write(f"Food Expense Report - generated {current_date}\n\n")
for date, amount in food_amount_dictionary.items():
    food_report.write(f"{date}: ${amount}\n")
food_report.write(f"Total: ${food_final_total:.2f}")
food_report.close()