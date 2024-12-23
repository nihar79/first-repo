def inputArrSize():
    numbers=[]
    flag=False
    try:
        arr_size=int(input("Enter array Size: "))
    except ValueError as e:
        flag=True
        print("Enter a valid array size")

    if not flag:
        numbers=input().split(" ")
        numbers=[int(x) for x in numbers]
    return numbers
    
def retValue(val,numbers):
    try:
        return numbers[val]
    except Exception as e:
        print("Index out of range")
    return -1

nums=inputArrSize()
if len(nums)>0:
    print(retValue(0,nums))