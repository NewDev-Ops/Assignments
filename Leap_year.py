test = int(input("Enter your year: "))

if test%4 == 0:
    if  test % 100 != 0 or test % 400 == 0:
        print("YES, it is a leap year")
    else:
        print("NO, it isn't a leap year")
else:
    print("NO, it is NOT a leap year")
