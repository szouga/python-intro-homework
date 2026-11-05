# Use a for loop with range() to calculate the sum of all integers from 1 to 100. Print the result.
# Example output — your message wording might differ:

# The sum of 1 to 100 is 5050.

total = 0
for i in range(1, 101):
    total += i
    
print(f" The sum of all integers from 1 to 100 is {total}.")