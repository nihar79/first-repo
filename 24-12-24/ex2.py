def print_nums(m,n):
    for i in range(m,n+1):
        print(i)

#print_nums(34,90)

def average(n):
    s=(n*(n+1))/2
    print("Average = ",s/n)

#average(10)

def pattern(m,n):
    for i in range(0,m):
        for j in range(0,n):
            print("#",end=" ")
        print("\n")

#pattern(2,8)

def do_something(m,n):
    for i in range(1,n+1):
        print(i+m)

#do_something(65,2)

def sum_ints(n):
    li=[]
    for i in range(0,n):
        li.append(int(input("Enter a number ")))
    print("Sum of Numbers",sum(li))

#sum_ints(3)                  

def pattern(n):
    for i in range(0,2):
        for j in range(0,n):
            for k in range(0,j+1):
                print(j+1, end=" ")
            print("\n")

#pattern(3)

def sum_of_squares(n):
    s=0
    for i in range(1,n+1):
        s += (i*i)
    print("Sum of squares is",s)

sum_of_squares(4)