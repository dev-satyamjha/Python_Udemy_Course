#all()

output: list[int] = [1,1,1,0,0,0]
print(all(output))

string: list[str] = ['Past', '', 'Gone', 'Fight']
print(all(string))

words: list[str] = ['System', 'Battery', 'Vehicle', 'Wife']
if all(words):
    print("The word list is not empty.")
else:
    print("The list is non-empty.")

print(all([]))

#any()

print(any(output))

script : list[str] = ['System', 'Battery', 'Vehicle', '']
if any(script):
    print("Script is getting prepared..")
else:
    print("Script hasn't started yet...!")

print(any([]))
