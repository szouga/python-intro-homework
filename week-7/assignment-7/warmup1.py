from pathlib import Path

#find the folder where this script is located
script_dir = Path(__file__).parent


#navigate up to the directory folder then into the data folder
file_path = script_dir.parent / 'data' / 'notes.txt'

with open(file_path, 'r') as file:
    index = 1
    for line in file:
        line = line.strip()
        print(f"Line {index}: {line}")
        index += 1
    
