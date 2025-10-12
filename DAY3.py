#Lists
elements: list[str]= ['Allu Arjun','Ram Charan','Keerthy Suresh','Unni Mukundan','Priyanka Mohan', 'Niveditha Thomas']
numbers: list[int] = [1,2,3,12,7,8]
mix: list[int|str] = [1, 'Bob', 2, 'John']

#list operations
numbers.append(5) #single append
print(numbers)
numbers.extend([18,36,54]) #multiple append
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop() #pops the last element
print(numbers)
popped: int = numbers.pop(3)
print(popped)
print(numbers)
mix.insert(3,'Satyam') #insert element at 3rd Index
print(mix)
mix[1] = 'Roman' #replace element at 1st index
print(mix)

#tuples
tuple1: tuple[int, str , bool] = (2,'Photo',True)
print(tuple1)
tuple2: tuple[int,...] = (1,2,3,4,5,5,6,7)
print(tuple2)
print(len(tuple2))

#sets
my_set: set[int] = {1,2,3,4,5,6,7,7,8,9,0,0}
print(my_set)
set_1: set[int | bool | str] = {1,2,3,4,0,5,True,False, 'Satyam', 'Roman'} #true and false are treated as duplicate values here
print(set_1)
set_2: set[int] = {1,4,7}
set_3: set[int] = {6,1,9}
set_2.add(5)
print(set_2)
set_3.remove(1)
print(set_3)
print(set_2.union(set_3))
print(set_2 | set_3)
set_4 : set[str] = {'Allu', 'Ram', 'NTR'}
set_4.update(['Nani', 'Unni'])
print(set_4)
set_5: set[int] = {12,10,9,5,7}
set_6: set[int] = {9,10,12,6,8}
print(set_5.intersection(set_6))
#set_5.intersection_update(set_6)
#print(set_5)
print(set_5.difference(set_6))
#set_6.difference_update(set_5)
#print(set_6)
print(set_5.symmetric_difference(set_6))
set_5.symmetric_difference_update(set_6)
print(set_5)

#frozen sets
fs: frozenset[int | str] = frozenset([1,2,3,4,'Happy','Passionate', 'Confident'])
print(fs)
name : set[str] = ({'Globe', 'India', 'Best'})
print(name | {f'Proud','Indian'})

#Dictionary

person: dict[str, str] = {'name': 'Satyam', 'occupation': 'Actor'}
print(person)
person: dict[str, str | int] = {'name': 'Satyam', 'age': 22}
print(person)
empty: str = dict() # Prints empty dictionary
print(empty)
person: dict[str, str | float] = {'name': 'Satyam', 'age': 22, 'height': 5.7, 'color': 'brown'}
print(person.keys())
print(person.values())
print(person.items())
print(list(person.values()))
print('Satyam' in person.values())
print(person[('name')])
print(person.get('age'))
print(person.get('Harsh'))
person['Gender'] = 'male'
print(person)
del person['height']
print(person)
person['Eyes'] = 'black'
print(person)
person.pop('Eyes')
print(person)
person.update({'name': 'Allu Arjun', 'age': 42,})
print(person)
A: dict[str, str] = {'name' : 'Satyam', 'dream': 'IAS', 'schooling' : 'no', 'college': 'yes'}
B: dict[str, str] = {'name': 'Harsh', 'dream': 'Normal person', 'schooling': 'no', 'college': 'yes'}
C = A | B
print(C)
