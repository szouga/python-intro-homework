print(not True and False) 
#^ not True is the same as False. False and False also means False, therefore
# line one will print False

print(True or False and False)
#^False and False just means False and True is a standalone statement
#because the or boolean operator states that either or can be true. Therefore,
#line five will print True or False

print(not (5 > 3))
#^This will print False. logic 5 > 3 or 5 is greater than 3, is a true statement
#the not operator makes the entire statement claim "not True"

print(10 == 10 and 4 != 4)
#^This will print False the logic on the left is true, but the logic on the right is false,
#and when a true logical statement is combined, or the and boolean operator is implemented,
#with a false logical statement, the entire expression becomes False.

print(not False or not True)
#^this will print True or False. 
#the boolean operators, not, make the left expression True and the expression
#on the right False
