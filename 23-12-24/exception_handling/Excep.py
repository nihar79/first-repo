a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Second parameter cannot be Zero", e)
except Exception as e:
    print(e)

print("=========PROGRAM COMPLETED===========")