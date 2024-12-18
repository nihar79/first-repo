ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
print("The original list is", ages)

ages.sort()

print("The sorted list is", ages)

print("The minimum age is", min(ages))
print("The maximum age is", max(ages))

ages.append(min(ages))
ages.append(max(ages))
print("Added min and max ages to the list",ages)

ages.sort()
ages_len=len(ages)

if ages_len%2==0:
    median=(ages[ages_len//2-1]+ages[ages_len//2])/2
    print("The median age is",median)
else:
    median=ages[ages_len//2]
    print("The median age is",median)

average_age=sum(ages)/ages_len
print("The average age is", average_age)

print('The range of ages is', max(ages)-min(ages))

lower_deviation=abs(min(ages)-average_age)
print('The lower deviation is',lower_deviation)
higher_deviation=abs(max(ages)-average_age)
print('The higher deviation is',higher_deviation)

#comparing
print('The comparison in deviation is', abs(lower_deviation-higher_deviation))


countries=['China', 'Russia', 'USA', 'India', 'Sweden', 'Norway', 'Denmark']

countries_len=len(countries)

if countries_len%2==0:
    print("The middle countries are",countries[countries_len//2-1],"and",countries[countries_len//2])
else:
    print("The middle country is",countries[countries_len//2])

list1=countries[0:countries_len//2]
list2=countries[countries_len//2:]

print("The first list is",list1)
print("The second list is",list2)

scandic=countries[0:3]
non_scandic=countries[3:]

a,b,c=scandic
x,y,z,w=non_scandic

print("The scandic countries are",a,b,c)
print("The non-scandic countries are",x,y,z,w)