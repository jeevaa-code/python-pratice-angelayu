# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆



#Write your code below this row 👇
Total_count = 0
sum_of_height = 0
for i in student_heights:
  Total_count += 1
  sum_of_height += i
print(round(sum_of_height/Total_count))
