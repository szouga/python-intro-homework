# Using loops and data structure operations, your script must:

# Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
# Calculate the class average — accumulate the total score in a loop, then divide.
# List all unique subjects — use a set to collect subjects as you loop, then print them.
# List high scorers — use a loop and .append() to get the names of all students who scored above 75.


students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
student_scores = 0

for student in students:
    
    if student['score'] > student_scores:
        student_scores = student['score']
        student['name'] = student['name']
        student_information = f"Student: {student['name']} Score: {student['score']}"
    else:
        continue
print(f"Top Scorer: {student_information.replace("Student:","")}")
    
score = 0
for student in students:
    score += student['score']
class_average = score/len(students)
print(f"Class Average: {class_average:.2f}")

subjects = []
for student in students:
    subjects.append(student['subject'])
subjects_set = set(subjects)
print(f"Subjects offered: {subjects_set}")

high_scores = []
for student in students:
    if student['score'] > 75:
        high_scores.append(student['name'])
print(f"High Scorers: {high_scores}")
# High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']