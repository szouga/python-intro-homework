def find_min(numbers):
    """find the minimum value from the numbers given"""
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers[0]
    
def find_max(numbers):
    for i in range(len(numbers)):
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    return numbers[0]
    
def search(numbers, target):
    index = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            index = i
            break
    return index

def bubble_sort(numbers):
    bubble_sort_list = []
    
    for i in numbers:
        bubble_sort_list.append(i)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(bubble_sort_list)-1):
            #bubble_sort_list.append(i)
            if bubble_sort_list[i] > bubble_sort_list[i + 1]:
                bubble_sort_list[i], bubble_sort_list[i + 1] = bubble_sort_list[i + 1], bubble_sort_list[i]
    
                swapped = True


    return bubble_sort_list
    
    
    
def check_option(userchoice, numbers):
    """purpose of this function is to keep the while loop"""
    if userchoice == 1:
        return find_min(numbers)
        
        
        
    elif userchoice == 2:
        return find_max(numbers)
        
        
    
    elif userchoice == 3:
        target = int(input("Type a random number: "))
        # Capture the three values coming out of the search function
        index = search(numbers, target)
        
        # Return them out of check_option so main can see them
        return index
                        
    elif userchoice == 4:
        bubble_sorted = bubble_sort(numbers)
        return bubble_sorted
        
        
    
    elif userchoice == 5:
        return "Goodbye"
        

        
def show_menu():
    user_input = (input(
                                                "=== Number Cruncher ===\n"
                                                "   1. Find minimum     \n"
                                                "   2. Find maximum     \n"
                                                "   3. Search for a number\n"
                                                "   4. Sort the list    \n"
                                                "   5. Quit     \n"
                                                "   Choose an option (1-5): "
                                                ))
    return user_input

def main():
    #show_menu()
    #menu runs continuously
    while True:
        #show_menu()
        try:
                                
                        
            #place input menu inside loop so it displays every time
            user_input = show_menu()
                                    
                                
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input > 5 or user_input < 1:
                    print("Error number too large or too small choose an option between 1-5")
                            
                        #if user chose an option 1-4 one of the branches should run if not the else statement 
                        # that represents the fifth option should run
                        #other functions will not be called unless user
                        #follows instructions
                            
                        
                else:
                    numberslist = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    
                    #these variables should only be used if user chooses option 3
                    
                    if user_input == 5:
                        print(check_option(user_input, numberslist))
                
                        break
                    elif user_input == 4:
                        bubble_sorted_list = check_option(user_input, numberslist)
                        print(bubble_sorted_list)
                        
                    elif user_input == 3:
                        index = check_option(user_input, numberslist)
                        if index == -1:
                            print(f"Number not found {index}")
                                                
                        elif index >= 0:
                            print(f"Target was found at index: {index}")
                            #^return -1, represents target not found
                            ## If target is None, it means this means user chose option 1, 2, 4, or 5
                            #and nothing this script should not run
                    elif user_input == 2:
                        print(f"The maximum number is {check_option(user_input, numberslist)}")
                    elif user_input == 1:
                        print(f"The minimum number is {check_option(user_input, numberslist)}")
                    
                                
                            
                            
                        
            
            
        except ValueError as ve:
            print(f"{ve} Please input a valid number options are 1-5")
    
            
    
    
main()