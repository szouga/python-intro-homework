# Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
# Print each key-value pair using .items() in a for loop
# Add a new key "graduated" with the value False
# Print the updated dictionary

gradebook = {
    'name': 'James',
    'grade': 98,
    'subjects': ['history', 'english', 'math', 'cooking', 'programming']
    
}

for key, value in gradebook.items():
    print(f"{key.title()}: {value}")
    
gradebook['graduated'] = False
print(gradebook)
