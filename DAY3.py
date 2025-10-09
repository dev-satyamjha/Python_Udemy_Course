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
