#import os
import csv
from pathlib import Path

#number one: Wrap the file opening in try/except FileNotFoundError. 
# If the file is missing, print an error message and stop.

#file path project file currently in 
script_dir = Path(__file__).parent

#file path to retrieve messy data file
messy_data_file_path = script_dir.parent / 'data' / 'messy_data.csv'

try:
    #script_dir = Path(__file__).parent
    with open(messy_data_file_path, 'r') as file:
        reader = csv.DictReader(file)
        skipped_rows = []
        parsed_rows = []
        rows_attempted = 0
        for row_num, row in enumerate(reader, start=1):
            rows_attempted += 1
            try:
                if None in row:
                    raise KeyError("Missing column in row")
                
                
                amount = float(row['amount'])
                
                parsed_rows.append(row)
            except (ValueError, KeyError) as e:
                if isinstance(e, ValueError):
                    skipped_rows.append(f"Row {row_num}: ValueError could not convert '{row['amount']}' to float")
                elif isinstance(e, KeyError):
                    skipped_rows.append(f"Row {row_num}: Missing or extra column detected - skipped")
                #skipped_rows.append(row)
                continue
                #append skipped rows to skipped list
            
            #print(row['name'], row['category'], row['amount'])
            #print(f"{skipped_rows}\n\n{parsed_rows}\n\n{rows_attempted}")

        print("=== CSV Report ===")
        print(f"Rows attempted: {rows_attempted}")
        print(f"Rows parsed: {len(parsed_rows)}")
        print(f"Rows skipped: {len(skipped_rows)}")
        print("\nSkipped rows:")
        for i in skipped_rows:
            print(f"\t{i}")
        
        print("\nClean Data:")
        for collection in parsed_rows:
            print(f"\t{collection['name']} | {collection['category']} | ${float(collection['amount']):.2f}")
            
except FileNotFoundError:
    print("File not found. Try again")