a=10
b=20
if(a>b):
    print("Greater")
elif(a<b):
    print("Lesser")
elif(a==b):
    print("Equals")
else:
    pass

#single line if-else
print("True") if a==b else print("False")

#if else using range function
print("Within Range") if a in range(0,10) else print("Out of range")

for i in range(0,21):
    #breakpoint()
    if i%5==0:
        continue
    print(i)

a=0
while(a<21):
    print(a)
    a += 1

#looping over dictionaries
a1= {
    '101':'abc',
    '102':'bcd',
    '103':'cde',
    '104':'def'
}

for key, value in a1.items():
    print(key, value)

#looping over tuples
a2=(2,8,'hello')
for element in a2:
    print(element)

#looping over sets
a3={1,3,4,5,9}
for element in a3:
    print(element)

