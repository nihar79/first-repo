def mul(n):
    return n*3

#n=int(input("Enter a Number "))
#print(n,"* 3 =",mul(n))

def is_multiple_of_7(num):
    if num%7==0:
        print("Divisible by 7")
    else:
        print("Not divisible by 7")

#is_multiple_of_7(343)
#is_multiple_of_7(90)

def in_range_200_500(n):
    if n>=200 and n<=500:
        print("Yes")
    else:
        print("No")

#in_range_200_500(267)
#in_range_200_500(888)

def get_discount(amount):
    discount=0.0
    if amount<500:
        discount=amount-(amount*0.05)
    elif amount>=500 and amount<2500:
        discount=amount-(amount*0.1)
    elif amount>=2500:
        discount=amount-(amount*0.2)
    return "Discounted Price = "+str(discount)
#print(get_discount(350))
#print(get_discount(900))
#print(get_discount(3000))

def show_number(n):
    for i in range(0,n+1):
        if i%2==0:
            print("Even",i)
        else:
            print("Odd",i)

#show_number(20)

def func(val):
    return val

#print(func("Hello Python!"))
#print(func(89.0))

def peri_square(side):
    return 4*side

#print("Perimeter =",peri_square(89))

def calculate_percentage(n):
    if n<1000:
        return 0.05*n
    else:
        return 0.1*n

#print(calculate_percentage(900))
#print(calculate_percentage(1100))

def get_speed_status(s):
    if s<60:
        return "Normal"
    elif s>=60 and s<80:
        return "Warning"
    else:
        return "Over Speed"

#print(get_speed_status(45))
#print(get_speed_status(75))
#print(get_speed_status(100))

def count_of_uppercase(s):
    freq=0
    for letter in s:
        if letter >= 'A' and letter <= 'Z':
            freq += 1
    return freq

#print(count_of_uppercase("chsc bMBSDMFHS bdjbBJDHBJS")) 

def validate_atm_pin_code(pin):
    pin=str(pin)
    if len(pin)==4 or len(pin)==6:
        for digit in pin:
            if not (digit>='0' and digit<='9'):
                return "Not a valid PIN"
        return "Valid PIN"
    else:
        return "Not a Valid PIN"

#print(validate_atm_pin_code(123456))
#print(validate_atm_pin_code("abd85n"))

#CONDITIONALS

def result(marks):
    if marks > 50:
        print("PASS")
    else :
        print("FAIL")
    return ""

#print(result(65))

def square_rect(a,b,c,d):
    if a==b and a==c and a==d:
        print("Square")
    else:
        print("Rectangle")
    return ""

#print(square_rect(1,2,3,5))
#print(square_rect(4,4,4,4))

def check_temp(temp):
    if temp>=15 and temp<=40:
        print("Can go for a Walk")
    else:
        print("Cannot go for a Walk")

#check_temp(25)
#check_temp(45)

def team(a,b):
    if (a > 300 or b > 300) and a + b < 500:
        print("Can Team Up")
    else:
        print("Cannot Team Up")

'''team(312,100)
team(100,312)
team(200,300)'''

def is_valid_triangle(a,b,c):
    if a+b+c<180:
        print("Valid Triangle")
    else:
        print("Not a Valid Triangle")

#is_valid_triangle(90,43,23)
#is_valid_triangle(90,90,3)

def bonus(salary,years):
    if years > 5:
        print("You will get a bonus of",salary*0.05)
    else:
        print("You will not get a bonus")

#bonus(10000000,6)
#bonus(7800,3)

def special_number(num):
    if num < 10 or num > 99:
        print("Please enter a Valid 2 digit number")
    else:
        digit1=num/10
        digit2=num%10
        if (digit1 + digit2 == 7) or (digit1==7 or digit2==7) or (num%7==0):
            print("The number is special")
        else:
            print("The number isn't special")

"""special_number(63)
special_number(70)
special_number(8)
special_number(25)"""

def special_string(s):
    if len(s) < 3:
        print("Not a special string")
    else:
        if s[0:3]=="NXT":
            print("Special String")
        elif is_special(s[3:]):
            print("Special String")
        else:
            print("Not a special string")

def is_special(s):
    for c in s:
        if c >= '0' and c <= '9':
            if int(c) % 2==0 or int(c) % 7==0:
                return True
    return False

"""special_string("abc297")
special_string("NXTjadgjh")
special_string("ehfr")"""

def square(num):
    if (num%10)==((num*num)%10):
        print("True")
    else:
        print("False")

"""square(5)
square(0)
square(7)"""

def check_num(a,b):
    if a*a+b*b >= 60:
        print(True)
    else:
        print(False)

"""check_num(3,4)
check_num(7,7)"""