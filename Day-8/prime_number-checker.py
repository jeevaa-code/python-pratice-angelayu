z = int(input())

if z == 2 :
    print("It is a prime number")
if z == 3 :
    print(" It is  a prime number")
if z == 1:
    print("it is not a prime nor number")
is_prime = True
if(z != 2 and z !=3 and z != 1):
    for i in range(2,z):
        if z%i == 0:
            is_prime = False
    if (is_prime):
        print("It is a prime number")
    else:
        print("It is not a prime number")