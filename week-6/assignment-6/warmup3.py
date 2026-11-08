# Demonstrate variable scope with two short examples in one file:

# Define a variable inside a function. 
# Try to access it outside the function and show the NameError 
# — paste the error in a comment, then remove or comment out the line that causes it.
# Show how return solves the problem: 
# return the value from the function and assign it to a variable in the outer scope. 
# Print it to confirm it worked.

#
def fibonacci_sequence(full_sequence):
    #sequence = f(n) = f(n - 1) + f(n - 2)
    n = 0
    index= 0
    position_sequence_list = []
    value_sequence_list = []
    for index in range(full_sequence):
        position_sequence_list.append(index)
        if index <= 1:
            n = n + index
        else:
            #n = n
            #n = (n-1) + (n-2)
            #n = (n + index) -1
            
            #the value sequence list should now state 0 1 1 start from the second position
                #and subtract from the number before it
            first_value = value_sequence_list[index-1]
            second_value = value_sequence_list[index-2]
            n = first_value + second_value
                            
        value_sequence_list.append(n)
        index += 1
    
    sequence = f"Position: {position_sequence_list}\nValue:{value_sequence_list}"
    return sequence

#print(sequence)
#NameError: line 12, in <module>
#     print(sequence)
#           ^^^^^^^
# NameError: name 'sequence' is not defined

full_sequence = fibonacci_sequence(8)
print(full_sequence)