#level1
age=int(input("Enter your age: "))

print("You are old enough to drive") if age>=18 else print("You need",18-age,"more years to learn to drive")

my_age=22
your_age=int(input("Enter your age: "))

if your_age>my_age:
    diff=your_age-my_age
    if diff==1:
        print("You are one year older than me")
    else:
        print("You are",diff,"years older than me")
elif your_age==my_age:  
    print("We are the same age")
else:
    diff=my_age-your_age
    if diff==1:
        print("I am one year older than you")
    else:
        print("I am",diff,"years older than you")

a=int(input("Enter first number "))
b=int(input("Enter second number "))

if a>b:
    print(a,"is greater than",b)
elif a==b:
    print(a,"is equal to",b)
else:
    print(a,"is less than",b)

#level2
score=int(input("Enter your score "))
if score in range(90,101):
    print("Grade A")
elif score in range(70,90):
    print("Grade B")
elif score in range(60,70):
    print("Grade C")
elif score in range(50,60):
    print("Grade D")
else:
    print("Grade F")


autumn=["SEPTEMBER","OCTOBER","NOVEMBER"]
winter=["DECEMBER","JANUARY","FEBRUARY"]
spring=["MARCH","APRIL","MAY"]
summer=["JUNE","JULY","AUGUST"]

season=input("Enter a month: ")
season=season.upper()
if season in autumn:
    print("Autumn")
elif season in winter:
    print("Winter")
elif season in spring:
    print("Spring")
elif season in summer:
    print("Summer")
else:
    print("Please enter a valid season")

fruit=input("Enter a fruit: ")
fruits=['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
    fruits.append(fruit)
    print("Modified list",fruits)
else:
    print("Fruit already present")

#level3
person={ 
    'first_name': 'Python', 
    'last_name': 'Program', 
    'age': 250, 
    'country': 'India', 
    'is_marred': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'address': { 
        'street': 'Space street', 
        'zipcode': '02210' 
    } 
    }

person_keys=person.keys()
if "skills" in person_keys:
    skills=person.get('skills')
    skill_len=len(skills)
    if skill_len%2==0:
        print("Middle skills are",skills[skill_len//2-1],"and",skills[skill_len//2])
    else:
        print("Middle skill is",skills[skill_len//2])

skills=person.get('skills')
print("Python is present") if 'Python' in skills else print("Python not present")

if len(skills)==2:
    if 'JavaScript' in skills and 'React' in skills:
        print('He is a frontend developer')
elif len(skills)==3:
    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    elif 'Node' in skills and 'Python' in skills and'MongoDB' in skills:
        print('He is a backend developer')
else:
    print('Unknown title')

