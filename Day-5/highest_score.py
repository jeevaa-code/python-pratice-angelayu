# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

max_score = 0
for i in student_heights:
    if i >= max_score:
         max_score = i
print(max_score)