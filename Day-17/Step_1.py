'''
class is a blue_print
class every first letter should be capitalized...
'''


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        ''' where we are going to construct...
        init function is going to call every time when object is created..'''
        print("user is created")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("01", "jeevaa")
user2 = User("02", "balaji")

user1.follow(user2)

print(user1.following)
print(user2.followers)

#print(user1.username)
#print(user2.id)
#print(user1.followers)


def functon():
    pass


'''attribute it is a variable associated with a object...'''

user1.id = "001"
user1.name = "jeevaa"

'''for user 2 to user 100 we need to add id and name to make it simpler.. constructor come into play
constructor is a part of a blueprint - object being constructed...
It is also known as intializing
__init__ function intializes the construction every the object created...'''
