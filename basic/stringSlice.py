### 文字列操作いろいろ、スライス、置換、

import string

letters = string.ascii_lowercase
print(letters)
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])
print(len(letters))

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But That is liquid which is moist and wet
Fire that property can never get.
Then 'tis not could that doth the fire put out
But 'tis the wet that makes it die, no doubt'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('Thats all, folds!'))
print(poem.find('the'))
print(poem.rfind('the'))
print(poem.count('the'))
print(poem.isalnum())

# Exception
# print(letters[100])
# name = 'Henny'
# name[0] = 'P'

print("\n###slice")
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[4:20:3])
print(letters[19::4])
print(letters[::-1])

print('\n### split & join')
todos = 'get gloves, get mask , give cat vitamins , call ambulance'
print(todos.split(','))
print(todos.split())

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing bool dials: ', crypto_string)

print('\n### change & replace')
setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))
print(setup.replace('duck', 'marmoset'))



