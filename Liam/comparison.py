# comparison.py
userAge = int(input("enter your age:"))

if userAge > 10 and userAge < 13:
    print("youre a tween")

if userAge <= 10:
    print("you are babby")

if userAge >= 13 and userAge <= 19:
    print("youre a teenager")
else:
    print("you're old")
