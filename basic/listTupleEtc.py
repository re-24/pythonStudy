### リスト、タプル、辞書、dictionary、集合

### list
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday']
another_empty_list = list()

print(empty_list)
print(weekdays)
print(another_empty_list)
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))
birthday = '1/6/1952'
print(birthday.split('/'))

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
print(marxes[0:2])
print(marxes[::2])
marxes.append('Zappo')
print(marxes)

others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
marxes += others
print(marxes)
marxes.append(others)
print(marxes)
marxes.insert(3, 'Gummo')
print(marxes)
del marxes[-1]
print(marxes)
marxes.remove('Gummo')
print(marxes)
print(marxes.pop())
print(marxes)
print(marxes.index('Wanda'))
print('Groucho' in marxes)
print('Bob' in marxes)
print(','.join(marxes))
sorted_marxes = sorted(marxes)
print(sorted_marxes)
marxes.sort()
print(marxes)

# copy いろいろ
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'test'
print(a, b, c, d)

### tuple
empty_tuple = ()
print(empty_tuple)
one_marxes = 'Groucho',
print(one_marxes)
one_marxes = ('Groucho',)
print(one_marxes)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
a, b, c = marx_tuple
print(a,b,c)

### 辞書
empty_dict = {}
print(empty_dict)
bience = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bience)

lol = [['a', 'b'],['c', 'd'],['e', 'f']]
print(dict(lol))

pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)
others = {'Marx': 'Groucho', 'Howard': 'moe'}
pythons.update(others)
print(pythons)
del pythons['Howard']
print(pythons)
# pythons.clear()
# print(pythons)

print(pythons['Cleese'])
# print(pythons['AAA']) # exception
print(pythons.get('AAA', 'Not a python'))
print(pythons.keys())

# set
empty_set = set()
print(empty_set)

even_number = {0,2,4,6,8}
print(even_number)
odd_number = {1, 3, 5, 7, 9}
print(odd_number)

print(set ('letters'))

drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'vodka', 'kahlua', 'cream'},
    'manhattan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' : {'orange juice', 'vodka'},
}

for name , contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print (name)

bruss = drinks['black russian']
wruss = drinks['white russian']

print(bruss & wruss)
print(bruss.intersection(wruss))
print(bruss | wruss)
print(bruss.union(wruss))
