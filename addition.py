def addition(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Sum is:", total)

addition()

addition(1,2,3,4,55)


addition(1,2,3,2.5,30)
