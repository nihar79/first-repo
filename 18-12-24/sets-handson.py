

it_companies= {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#level 1
it_companies_len=len(it_companies)
it_companies.add('Twitter')
it_companies.update(('Tesla','Uber','Netflix'))
#it_companies.remove('Nasa') exception
it_companies.discard('Nasa') #no exception

#level2
A={19, 22, 24, 20, 25, 26}
B={19, 22, 20, 25, 26, 24, 28, 27}

C=A.union(B)
D=A.intersection(B)
isSubset=A.issubset(B)
areDisjointSets=A.isdisjoint(B)
E=C.union(B.union(A))
F=A.symmetric_difference(B)
A=None
B=None

#level3
ages_list= [22, 19, 24, 25, 26, 24, 25, 24]
ages=set(ages_list)
print("Age list is bigger") if len(ages_list)>len(ages) else print("They are equal")
sen="I am a teacher and I love to inspire and teach people"
uniq_words=len(set(sen.split()))
print(uniq_words)