class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


jeevaa = User("001", "Jevvaananthan_JKS")
deva = User("002", "Devaraj")
print(jeevaa.id)
jeevaa.follow(deva)
print(jeevaa.following)
print(deva.followers)
'''every time when a user need to create for every user we need to add id, username
 It is not a fessible way '''

'''To solve this solution name is constructor...
   This also known as initializing the object...
   we done it by special function known as __init__ function...
   init function is going to call everytime a object created from the function
   self is a actual object being created and being initialized'''

'''attributes are object has
   methods are object does'''
