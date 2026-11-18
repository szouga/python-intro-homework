try:
    with open("missing.txt", "r") as missing_file:
        reader = missing_file.read()
        print(reader)
except FileNotFoundError as fe:
    print(f"{fe}: file was not found. Try using the os or pathlib modules to find the file")
