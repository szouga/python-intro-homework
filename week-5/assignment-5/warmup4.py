#FizzBuzz for multiples of both 3 and 5
#Fizz for multiples of 3 only
#Buzz for multiples of 5 only
#and the number itself otherwise (if doesn't meet the conditions above)
#the combined case is checked first, so 15 and 30 print FizzBuzz.

combined_case = []
#^holds only 15 and 30
multiples_three = []
#^holds only multiples of three
multiples_five = []
#^holds only multiples of five

fizzbuzzfinaloutcome = []
for i in range(3,31,3):
    multiples_three.append(i)
#outputs 3-30 multiples of 3 only

for i in range(5, 31, 5):
    multiples_five.append(i)
#outputs 5-30 multiples of 5 only


for i in multiples_three:
    for j in multiples_five:
        if i == j:
            combined_case.append(i)

for i in range(1,31):
    if i in combined_case:
        fizzbuzzfinaloutcome.append("FizzBuzz")
    elif i in multiples_three:
        fizzbuzzfinaloutcome.append("Fizz")
    elif i in multiples_five:
        fizzbuzzfinaloutcome.append("Buzz")
    else:
        fizzbuzzfinaloutcome.append(i)

for i in fizzbuzzfinaloutcome:
    print(i)
#print each individual item on a separate line instead of in a list