flag=False
try:
    num=int(input("Enter a Number "))
except ValueError as e:
    flag=True
    print("Entered input is not a valid format for an integer")
except Exception as e:
    print(e)

if not flag:
    print("Square is: ",num*num)
