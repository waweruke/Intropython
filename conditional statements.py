age = 21
if age < 18:
    print("True")
else:
    print("False")


    x = 10
    y = 20
    if x < y and y > 30 :
        print("TRUE")
    else:
        print("FALSE")

        if x < y or y > 50:
            print("TRUE")
        else:
            print("FALSE")


            marks = 90
            if marks < 40:
                print("E")
            elif marks < 50:
                print("D")
            elif marks < 60:
                print("C")
            elif marks < 70:
                print("B")
            else:
                print("A")




bettingNumber = 2
if  bettingNumber == 1:
    print("you won a goat!!")
elif bettingNumber == 2:
    print("you won a cow!!")
elif bettingNumber == 3:
    print("you won 3 cows!!")
elif bettingNumber == 4:
    print("you won 5 cows!!")
else:
    print("please enter a number from 1 - 4 to bet!!")


weight = 70
height = 1.5
BMI = (weight / (height * height))
if BMI < 18:
    print("underweight")
elif BMI < 29:
    print("normalweight")
elif BMI < 34:
    print("overweight")
else :
    print("obese")



p = 1000
r = 15
t = 2
interest = (p * r * t)/100
if interest < 250:
    print("BADLOAN")
elif interest <10000:
    print("GOODLOAN")
else:
    print("SCAM")


