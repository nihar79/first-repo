dog={}

dog['name']='Aurum'
dog['color']='Brown'
dog['breed']='German Shephard'
dog['legs']=4

student={
    'firstname':'Xavier',
    'lastname':'Cross',
    'gender':'Male',
    'age':18,
    'marital-status':'Single',
    'skills':['Math','Science','Football'],
    'country':'US',
    'city':'Florida',
    'address':'123 Newark'
}

print(len(student))

print("Skills is a list") if isinstance(student['skills'],list) else print('Not a list')

student['skills'].extend(['Cooking','Cleaning'])

print(student.keys())
print(student.values())

student_details=[]
for key,value in student.items():
    temp=(key,value)
    student_details.append(temp)

print(student_details)

student.pop('address')
print(student)

student=None

