# Command: python warmup1.py
# Output:  Python is working!

# write a script that prints the following message
# Python is working!


def output_script(first_output, second_output, third_output):
    string_third_output = []
    first_output = first_output.replace("-","").capitalize()
    
    second_output = second_output.strip(" ")
    second_output = second_output[:-1]
    
    third_output.reverse()
    for i in third_output:
        string_third_output.append(i)
    string_third_output = "".join(string_third_output)
    
    
    return f"{first_output} {second_output} {string_third_output}!"
    
    
pyth_n = "p-y-t-h-o-n"
iss = " iss "
working = ["g","n","i","k","r","o","w"]

print(output_script(pyth_n, iss, working))