#!/usr/bin/env python3

message = 'BASED ON YOUR SCORE, YOUR GRADE IS : '

# let's get your scoere
score = int(input("What is your SCORE?? : "))

# if input value was higher or equal to 25
if score >= 90:
    message = message + 'A - Excellet'
elif score >= 89:
    message = message + 'B - Great'
elif score >= 79:
    message = message + 'C - Good'
elif score >= 69:
    message = message + 'D - Poor'
else:
    message = message + 'F- Failed'
print(message)

