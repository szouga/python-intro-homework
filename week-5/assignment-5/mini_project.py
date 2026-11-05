def menu():
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

    
    #menu runs continuously
    try:
        while True:
                #place input menu inside loop so it displays every time
                    
                user_input = int(input(
                                        "=== Number Cruncher ===\n"
                                        "   1. Find minimum     \n"
                                        "   2. Find maximum     \n"
                                        "   3. Search for a number\n"
                                        "   4. Sort the list    \n"
                                        "   5. Quit     \n"
                                        "   Choose an option (1-5): "
                                        ))
                
                if user_input > 5 or user_input < 1:
                    print("Error number too large or too small choose an option between 1-5")
                    continue
                #if user chose an option 1-4 one of the branches should run if not the else statement 
                # that represents the fifth option should run
                elif user_input in range(1,5):
                    if user_input == 1:
                        for i in range(len(numbers)):
                            min_index = i
                            for j in range(i + 1, len(numbers)):
                                if numbers[j] < numbers[min_index]:
                                    min_index = j
                            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
                        print(f"The minimum number is {numbers[0]}")
                        #no break present so automatically loops back to the menu
                    elif user_input == 2:
                        for i in range(len(numbers)):
                            max_index = i
                            for j in range(i + 1, len(numbers)):
                                if numbers[j] > numbers[max_index]:
                                    max_index = j
                            numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
                        print(f"The maximum number is {numbers[0]}")
                    elif user_input == 3:
                        user_number = int(input("Type a random number: "))
                        found = False
                        found_index = -1
                        for i in range(len(numbers)):
                            if numbers[i] == user_number:
                                found = True
                                found_index = i
                                break
                        if found:
                            print(f"Your number, {numbers[i]}, was found at index: {found_index}")
                        else:
                            print(f"Number not found")
                        
                    elif user_input == 4:
                        swapped = True
                        while swapped:
                            swapped = False
                            for i in range(len(numbers)-1):
                                if numbers[i] > numbers[i + 1]:
                                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                                    swapped = True
                        print(numbers)
                else:
                    print("Goodbye")
                    break
        
    except ValueError as ve:
        print(f"{ve} Please input a valid number options are 1-5")
        menu()
menu()