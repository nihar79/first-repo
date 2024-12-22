import math

def add_two_numbers(x,y):
    return x+y

def circle_area(r):
    return (22*r*r)/7

def add_all_nums(*numbers):
    total=0
    flag=False
    for number in numbers:
        if(isinstance(number,'int')):
            total += number
        else:
            flag=True
            break

    if(flag):
        print('Please give appropriate input')
    else:
        print('The total is:',total)

def convert_celsius_to_fahrenheit(c):
    return (c*9/5)+32

def slope(x,y,c):
    return (y-c)/x

def quadratic_solution_set(a,b,c):
    x1=(-b+math.sqrt(b*b-4*a*c))/2*a
    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
    return list(x1,x2)

def print_list(*my_list):
    for element in my_list:
        print(element,end=" ")

def reverse_list(*my_list):
    my_list=list(my_list)
    n=len(my_list)
    for i in range(0,n//2):
        temp=my_list[i]
        my_list[i]=my_list[n-i-1]
        my_list[n-i-1]=temp

    print(my_list)

reverse_list('A','B')

#level2
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Fact of",n,"is",fact)

#mean, median, mode, range, variance,standard_deviation

#level3
def id_prime(n):
    number_of_factors=2
    for i in range(2,n):
        if n%i==0:
            number_of_factors += 1
    
    if number_of_factors==2:
        print("Prime")
    else:
        print("Not a Prime")


def is_unique(*elements):
    elements_set=set(elements)
    if len(elements)==len(elements_set):
        print("All items are unique")
    else:
        print("All items are not unique")

def same_type(*elements):
    elements=list(elements)
    return all(type(x)==type(elements[0]) for x in elements)

