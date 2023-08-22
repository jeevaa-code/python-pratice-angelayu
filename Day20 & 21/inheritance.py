class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale,exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swim in the water")

    def breathe(self):
        super().breathe()
        print("Doing this in water")


''' we can just normally breathe by nemo.breathe() 
below we have changed something in the breathe method so only we did it'''

nemo = Fish()
nemo.breathe()
'''I just inherited everything here from animal just normally
 without any change incase we need to do change in method we will do..'''
print(nemo.num_eyes)
