import math


def motto ():
    print("Hello there is our motto")

motto()
motto()
motto()
motto()

def vision():
    print("Hello this is our vision")

vision()

def add():
    x = 10
    y = 20
    z = x + y
    print(z)

add()
add()


def avg(x, y, z):
    average = (x + y +z)/3
    print("your average is"+str(average))

avg(3,4,5)
avg(21,22,23)



def bmicalc(weight,height):
    bmi = weight / pow(height, 2)
    if bmi <= 18:
        print("underweight")
    elif bmi <= 29:
        print("normalweight")
    elif bmi <= 34:
        print("overweight")
    else:
        print("obese")

bmicalc(70, 1.2)

def grading(a, b, c,d):
    avgmark = (a + b + c + d)/4
    if avgmark < 40:
        print("E")
    elif avgmark < 50:
        print("D")
    elif avgmark < 60:
        print("C")
    elif avgmark < 70:
        print("B")
    else:
        print("A")

grading(50, 60, 70, 80)


def login (email ,password):
    if email =="user@example.com" and password =="user123":
        grading(40,50,70,80)
    else:
        print("loginfailed")

login("user@example.com", "user123")


def areaofacircle(radius):
    area = math.pi * pow(radius, 2)
    return area

print(areaofacircle(7))