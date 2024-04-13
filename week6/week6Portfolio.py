# VC
# 09-04-2024

exam_score = []

numStudents = int(input("Enter number of students: "))

for count in range(numStudents):
    marks = int(input("Enter marks of student: "))
    exam_score.append(marks) # adding every entry to the end of the list exam_scores

high = max(exam_score)
low = min(exam_score)
avg = int(sum(exam_score))/numStudents # divided total score by number of students
avg = round(avg,2)

print(f"The highest score is: {high}")
print(f"The lowest score is: {low}")
print(f"The average score is: {avg}")