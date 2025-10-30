# *args *kwargs
def greet(*person: str, greeting: str = 'Hey!'):
    print(person)
    for people in person:
        print(f"{greeting}{people}")
greet('Satyam', 'Allu Arjun', 'Roman')

def setup(Version : str , **kwargs):
    print('Version:', Version )
    print('Settings:', kwargs)

    if 'volume' in kwargs.keys():
        print(f"Volume set to: {kwargs.get('volume')}")
setup(Version='5.0', volume=15, System = 'Stereo', Brand = 'JBL' )

name: list[str] = ['Satyam', 'Keerthy', 'Priyanka', 'Niveditha', 'Roman']
settings: dict[str, float|str] = {'volume': 15, 'Brand':'JBL'}
print(*name, sep = ', ', end ='.\n')

def setup1(Version : str , **kwargs):
    print('Version:', Version )
    print('Settings:', kwargs)

    if 'volume' in kwargs.keys():
        print(f"Volume set to: {kwargs.get('volume')}")
setup1(Version='2.0', **settings )
