a = 10
b = 10
c = 10

"""
if a > b and a > c: # If this line is true then only control flow goes inside
    print("A is the biggest amongst a,b and c")
#    print("Yes, I want to tell again A is bigger")
elif b > a and b > c:
    print("B is biggest")
elif c > a and c > b:
    print("c is biggest")
else: # if the above condition fails then it goes to else
    print("All are equal")


env = "prd"

if env == "dev":
    print("Load dev application")
else:
    print("Not in dev environment")

""" 

def check_biggest(a,b,c):
    if a > b and a > c: # If this line is true then only control flow goes inside
        print("A is the biggest amongst a,b and c")
#       print("Yes, I want to tell again A is bigger")
    elif b > a and b > c:
        print("B is biggest amongst a,b and c")
    elif c > a and c > b:
        print("c is biggest amongst a,b and c")
    else: # if the above condition fails then it goes to else
        print("All are equal amongst a,b and c")

check_biggest(100,200,300)