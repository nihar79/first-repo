#level1

#empty tuple
tup=()

sisters=('A','B','C')
brothers=('X','Y','Z')
siblings=sisters.__add__(brothers)
number_of_siblings=len(siblings)
family_members=siblings.__add__(('Father','Mother'))

#level2
sib=tuple(set(family_members).difference({'Father','Mother'}))
parents=tuple(set(family_members).difference(set(sib)))

fruits=('apple','mango','bananas')
vegetables=('brinjal','tomato','potato')
animal_products=('milk','cheese')

food_stuff_tp=fruits.__add__(vegetables.__add__(animal_products))
print(food_stuff_tp)

food_stuff_lt=list(food_stuff_tp)

food_stuff_len=len(food_stuff_lt)

if food_stuff_len%2==0:
    mid1, mid2=food_stuff_lt[food_stuff_len//2-1], food_stuff_lt[food_stuff_len//2]
else:
    mid=food_stuff_lt[food_stuff_len//2]

first_three=food_stuff_tp[:3]
last_three=food_stuff_tp[food_stuff_len-3:]

food_stuff_tp=None

nordic_countries = ('Denmark', 'India','Iceland', 'Norway', 'Sweden')
print('Estonia is Nordic') if 'Estonia' in nordic_countries else print('Estonia is not Nordic')
print('Iceland is Nordic') if 'Iceland' in nordic_countries else print('Iceland is not Nordic')