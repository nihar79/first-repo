import copy
import math

#declaring an empty list
my_list=[]

my_list=[1,'apple',True,893.9,'IBM',[78,90]]
print("List of 5 items ",my_list)

my_list_len=len(my_list)
print('Length of my_list is ', str(my_list_len))

print("First item of the list is ", str(my_list[0]))

print("Middle item of the list is ", str(my_list[my_list_len//2]))

print("Last item of the list is ", str(my_list.pop()))

mixed_data_types=['Niharika',22,"5.5ft","Single","Lucknow UP"]

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print('The IT Comapnies are ',it_companies)

it_companies_len=len(it_companies)
print('The number of IT Companies is ',it_companies_len)

print('The first company is ',it_companies[0])
print('The middle company is ',it_companies[it_companies_len//2])
print('The last company is ',it_companies[it_companies_len-1])

it_companies[0]='Tesla'
print('Modified company list is ',it_companies)

it_companies.append('Open AI')
print('Updated IT Company list is ',it_companies)

it_companies.insert(it_companies_len//2,'Netflix')
print('The updated company list is ',it_companies)

it_companies[0]=it_companies[0].upper()
print('List of IT Companies with Upper Case company name ',it_companies)

print('Joined IT Companies are ', '#; '.join(it_companies))

company=input("Please enter company name to check ")
if company in it_companies:
    print('Company is present')
else:
    print('Company is not present')

it_companies_copy=copy.deepcopy(it_companies)
it_companies_copy.sort()
print('The sorted companies list is ',it_companies_copy)

it_companies_copy.reverse()
print('The reversed company list is ',it_companies_copy)

#updating the length
it_companies_len=len(it_companies)
print('The original list is ',it_companies)

print('First 3 companies are ', it_companies[0:3])
print('Last 3 companies are', it_companies[it_companies_len-3:])

if it_companies_len%2==0:
    print('Middle IT Companies are ', it_companies[it_companies_len/2-1:it_companies_len/2+1])
else:
    print('Middle IT Company is ',it_companies[(it_companies_len//2)])

it_companies.remove(it_companies[0])
print('The first company has been removed. Updated List: ', it_companies)

#updating length again
it_companies_len=len(it_companies)

if it_companies_len%2==0:
    it_companies.remove(it_companies[it_companies_len//2-1])
    #update length again
    it_companies_len=len(it_companies)
    it_companies.remove(it_companies[it_companies_len//2])
else:
    it_companies.remove(it_companies[it_companies_len//2])

print('The middle element(s) have been removed. Here is the updated list ',it_companies)

it_companies.pop()
print('The last company has been removed. Updated list is ',it_companies)

#removed all companies from the list
it_companies.clear()
print('Removed all companies from the list',it_companies)

#Destroyed the list. Memory deallocated
it_companies=None
print('Destroyed the list')

front_end=['HTML','CSS','JS','React','Redux']
back_end=['Node','Express','MongoDB']

front_end.extend(back_end)
print('The combined list is in front_end',front_end)

full_stack=copy.deepcopy(front_end)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print('The fullstack list is', full_stack)