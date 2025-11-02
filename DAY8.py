#User Input
name: str = input("Enter your name to get it converted into ascii: ").strip().capitalize()
print(name)
ascii= [ord(n) for n in name]
print (f"The name's ascii value is : {ascii}")
