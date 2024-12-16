prelim = eval(input("Input your on Prelim Grades: "))
midterm = eval(input("Input your Midterm Grades: "))
semi_final = eval(input("Input your Semi-final Grades: "))
final = eval(input("Input your Semifinal Grades: "))
quiz = eval(input("Input your Quiz Grades: "))
project = eval(input("Input your project Grades: "))

final_grades = (prelim * 0.15) + (midterm * 0.15) + (semi_final * 0.15) + (final * 0.15) + (quiz * 0.15) + (project * 0.15)

print (f"Your final grades is {final_grades}")

if final_grades>= 75 : 
              print("Congratulations, you passed the course / subject")

else:
              print("Sorry, you failed")