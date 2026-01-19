"""
Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the 
grading scheme we are using in this class. 

Percent(%) Grade
90 100       A
80 89        B
70 79        C
60 69        D
0 60         F
"""

score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    score = int(score)  # drop any decimal part

    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)


