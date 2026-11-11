import os

print(os.getcwd())
#^this prints current directory pathway

#current directory pathway stored
script_directory = os.path.dirname(os.path.abspath(__file__))


#have to go up one level (week-7) to find data folder, expenses file location and extract the data
parent_path = os.path.abspath(os.path.join(script_directory, ".."))


# create directory to data folder 
data_path = os.path.abspath(os.path.join(parent_path, "data"))

expenses_path = os.path.abspath(os.path.join(data_path, "expenses.csv"))

if os.path.exists(expenses_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    
    
expenses_path = os.path.join(parent_path, "data", "expenses.csv")
print(expenses_path)

