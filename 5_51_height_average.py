# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
number_of_students = 0
for student in student_heights:
    sum += student
    number_of_students += 1

average = sum / number_of_students

print(round(average))