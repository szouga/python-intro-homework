# Create a hardcoded list of 8 numbers. Without using any loops, print:

# The first item
# The last item (use a negative index)
# A slice containing only the middle four items
# The full list in reverse order
numbers = [1,2,3,4,5,6,7,8]

print(f"First:    {numbers[0]}")
print(f"Last:     {numbers[-1]}")
print(f"Middle:   {numbers[2:6]}")
print(f"Reversed: {numbers[-1::-1]}")
