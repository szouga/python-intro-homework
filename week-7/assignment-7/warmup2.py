from pathlib import Path
import csv

script_directory = Path(__file__).parent

file_path = script_directory.parent / 'data' / 'students.csv'

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")