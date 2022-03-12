from itertools import product

letters = 'AZ'

for string in product(letters, repeat=2):
    s = ''.join(string)
    print(s)