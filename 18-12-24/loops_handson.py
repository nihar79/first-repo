#level1
for i in range(0,11):
    print(i)

i=0
while(i<11):
    print(i)
    i+=1

for i in range(10,-1,-1):
    print(i)

i=10
while(i>-1):
    print(i)
    i-=1

for i in range(0,7):
    for j in range(0,i+1):
        print('#',end="")
    print(end="\n")

for i in range(0,7):
    for j in range(0,7):
        print('#',end=" ")
    print("\n")
    
for i in range(0,11):
    product=i*i
    print(i,"x",i,"=",str(product))

tech=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for t in tech:
    print(t)

for i in range(0,101,2):
    print(i)

for i in range(1,100,2):
    print(i)

#level2
s=0
for i in range(0,101):
    s+=i
print(s)

s=0
for i in range(0,101,2):
    s+=i
print(s)

s=0
for i in range(1,100,2):
    s+=i
print(s)

#level3
#can't download the datafile