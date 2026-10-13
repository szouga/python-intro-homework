day = input("What day is it? ").capitalize()
time = input("What time of day? ").lower()

#days used: Tuesday, Thursday, Saturday
#times used: morning (8am-10am), evening (8pm-10pm), dusk (4pm-6pm)

if (day != "Tuesday" and day != "Thursday" and day != "Saturday") or (time != "morning" and time != "evening" and time != "dusk"):
    if (day != "Tuesday" and day != "Thursday" and day != "Saturday") and (time != "morning" and time != "evening" and time != "dusk"):
        print("Sorry we don't have the day or time you are looking for, try these:")
        print("Days: Tuesday, Thursday, Saturday")
        print("Times: morning, evening, dusk")
        
    elif day != "Tuesday" and day != "Thursday" and day != "Saturday":
        print(f"Sorry a suggestion for the day: {day} is not available at this time.\nPlease try Tuesday, Thursday, or Saturday")
    else:
        print(f"Sorry a suggestion for your time: {time} isn't available currently\nPlease try: morning, evening, or dusk")
    
    
else:
    if day == "Tuesday":
        if time == "morning":
            print("      Suggestion    ")
            print("Morning: 8am-10am ☀️")
            print("Have an egg white omelette")
            print("Vibe for today: Nike")
            print("~ Pro Leggings (with pockets)\n~ Running Pack Vest\n~ Zenvy Short Sleeve Top\n~ Vomero Premium Shoes\n~ Ankle Socks")
            print("Ride a bike 🚲")
        elif time == "dusk":
            print("      Suggestion    ")
            print("Dusk: 4pm-6pm 🌆")
            print("Enter a coding tournament today!:")
            print("~ LeetCode Contests")
            print("~ Amazon Developer Hackathon")
        else:
            #last else clauses must be reserved for evening information
            print("      Suggestion    ")
            print("Evening: 8pm-10pm 🌃")
            print("Best time to eat at Denny's is in the evening!")
            print("      Order    ")
            print("~ French Toast Slam")
            print("~ Bacon Cheeseburger Sliders")
            print("~ Waffles")
            print("~ Seasoned Fries")
            print("~ Wavy Cut French Fries")
            print("~ Salmon with broccoli")
            print("~ Orange Juice")
            print("~ Bottled Water")
        
    elif day == "Thursday":
            if time == "morning":
                print("      Suggestion    ")
                print("Morning: 8am-10am ☀️")
                print("Guess what? The Museum is free all day in Houston!\nPut on a nice outfit and attend the Fine Arts Museum")
                print("Vibe for today: Elegance")
                print("Long skirt, ballet design flats, long sleeve top, minimal jewelry")
                
            elif time == "dusk":
                print("      Suggestion    ")
                print("Dusk: 4pm-6pm 🌆")
                print("Complete chores list:")
                print("~ Vacuum and clean the floor")
                print("~ Dust objects")
                print("Read a book:")
                print("~ They Called Us Enemy")
                print("~ The Giver")
                print("Play Video Games:")
                print("~ Donkey Kong 64")
                print("~ Forza Horizon 6")
                
            else:
                print("      Suggestion    ")
                print("Evening: 8pm-10pm 🌃")
                print("Ride an ATV")
                print("Eat a banana and ice cream before bed")
    #last day is saturday
    else:
        if time == "morning":
            print("      Suggestion    ")
            print("Morning: 8am-10am ☀️")
            print("Volunteer at a ranch and ride a horse 🐎 ")
            print("Vibe for today: Texas")
            print("~ Wrangler Jeans")
            print("~ Buckle Belt")
            print("~ Bandana")
            print("~ Cowboy Boots")
            print("~ Short Sleeve Top")
            print("~ Socks")
            
        elif time == "dusk":
            print("      Suggestion    ")
            print("Dusk: 4pm-6pm 🌆")
            print("Take a Texas Road Trip and on the way try Buccee's")
            print("  Buccees:  ")
            print("~ Beaver Nuggets")
            print("~ Brisket Sandwich")
            print("~ Smoothie")
            print("~ Chocolate")
            print("~ Fruit")
            
        else:
            print("      Suggestion    ")
            print("Evening: 8pm-10pm 🌃")
            print("Be a background actor in an upcoming movie.")

