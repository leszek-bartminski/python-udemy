# 🚨 Don't change the code below 👇
from re import A


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

a = 0

for score in student_scores:
    if score > a:
        a = score 
print(f"The highest score in the class is: {a}")