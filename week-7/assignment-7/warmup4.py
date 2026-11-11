from datetime import datetime

now = datetime.now()

current_date = now.strftime("%B %d, %Y")
print(f"Today is {current_date}.")