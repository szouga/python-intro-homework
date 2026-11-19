
notnumber = True
while notnumber:
    user_input = input("Type a number: ")
    
    try:
        #isinstance checks for the type 
        if not user_input.isdigit():
            raise ValueError
        
        if user_input.isdigit():
            notnumber =  False
            user_input = float(user_input)
            print(f"Your number {user_input}")
            break
            
        # user_input = input("Type a number: ")
        # continue

    except ValueError:
        print("Not a valid answer please type a numerical value. Try again: ")
        continue
        
    