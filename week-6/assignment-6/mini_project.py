def find_min(numbers):
    """find the minimum value from the numbers given"""
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print(f"The minimum number is {numbers[0]}")
    
def find_max(numbers):
    for i in range(len(numbers)):
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    print(f"The maximum number is {numbers[0]}")
    
def search(numbers, target, found=False):
    userchoice = 3
    index = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            found = True
            index = i
            break
    return index, target, found, userchoice

def bubble_sort(numbers):
    swapped = True
    bubble_sort_list = []
    while swapped:
        swapped = False
        for i in range(len(numbers)-1):
            #bubble_sort_list.append(i)
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    
                swapped = True
    for i in numbers:
        bubble_sort_list.append(i)  
    print(bubble_sort_list)
    #print(numbers)
    
    
def check_option(userchoice, numbers):
    """purpose of this function is to keep the while loop"""
    if userchoice == 1:
        find_min(numbers)
        
        
        
    elif userchoice == 2:
        find_max(numbers)
        
        
    
    elif userchoice == 3:
        target = int(input("Type a random number: "))
        # Capture the three values coming out of the search function
        index, target, found, userchoice = search(numbers, target)
        
        # Return them out of check_option so main can see them
        return index, target, found, userchoice
                        
    elif userchoice == 4:
        bubble_sort(numbers)
        
        
    
    else:
        print("Goodbye")
        

        
def show_menu():
    
    #menu runs continuously
    try:
        #while True:
                #place input menu inside loop so it displays every time
                    
                user_input = (input(
                                        "=== Number Cruncher ===\n"
                                        "   1. Find minimum     \n"
                                        "   2. Find maximum     \n"
                                        "   3. Search for a number\n"
                                        "   4. Sort the list    \n"
                                        "   5. Quit     \n"
                                        "   Choose an option (1-5): "
                                        ))
                if user_input.isdigit():
                    user_input = int(user_input)
                    if user_input > 5 or user_input < 1:
                        print("Error number too large or too small choose an option between 1-5")
                        
                    #if user chose an option 1-4 one of the branches should run if not the else statement 
                    # that represents the fifth option should run
                    #other functions will not be called unless user
                    #follows instructions
                        return -1, None, False, 0
                    
                    else:
                        numberslist = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
                        
                        if user_input == 3:
                            return check_option(user_input, numberslist)
                        check_option(user_input, numberslist)
                        
                    
        
        
    except ValueError as ve:
        print(f"{ve} Please input a valid number options are 1-5")
    
    return -1, None, False, user_input

if __name__ == "__main__":
    while True:
        #these variables should only be used if user chooses option 3
            index, target, found, userchoice = show_menu()
            userchoice = int(userchoice)
            
            if userchoice == 5:
                break
            
            if userchoice == 3 and found == True:
                print(f"Your number, {target}, was found at index: {index}")
            elif userchoice == 3 and found == False:
                print(f"Number not found {index}")
                #^return -1, represents target not found
                ## If target is None, it means this means user chose option 1, 2, 4, or 5
                #and nothing this script should not run
                
 