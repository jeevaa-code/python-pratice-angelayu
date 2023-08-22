'''
local variable
and
global variable
'''

enemies = 1 #global variable

def increase_enemies():
  enemies = 2 #local variable
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = "skelton" #global variable

def increase_enemies():
  enemies = "zombie" #local variable
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")