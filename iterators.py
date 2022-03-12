
from itertools import cycle
from time import time

'''Ex. №2'''

# def infinite(lst: list, tries: int) -> str:
#     a = cycle(lst)
#     temp_lst = []
#     for _ in range(tries):
#         temp_lst.append(str(next(a)))
#     return ''.join(temp_lst)
#
# numbers = [*range(1, 11)]
#
# print(infinite(numbers, len(numbers) * 2))

'''Ex. №3'''

# def show_letters(line: str) -> str:
#     yield from [letter for letter in line if letter.isalpha()]
#
# a = show_letters('3k2h34khkjh5kj36kh^*F*GB^VD^&%DS')
#
# try:
#     while True:
#         print(next(a), end= ' ')
# except StopIteration:
#     print('\nGengerator has ended.')

'''Ex. №4'''

# def fibonachi(n: int):
#     yield 1
#     yield 2
#     start = [1, 2]
#     for _ in range(n - 2):
#         start[0], start[1] = start[1], start[0] + start[1]
#     yield start[1]
#
# a = fibonachi(4)
#
# try:
#     while True:
#         print(next(a), end= ' ')
# except StopIteration:
#     print('\nGengerator has ended.')

'''Ex. №4'''

# def deck():
#     yield from [f'{i} {z}' for i in ['\u2660', '\u2665',
#          '\u2666', '\u2663'] for z in [*range(2, 11), 'J', 'Q', 'K', 'A']]
#
# a = deck()
#
# try:
#     while True:
#         print(next(a), end= ' ')
# except StopIteration:
#     print('\nGengerator has ended.')

'''Ex. №5'''

# class CardDeck:
#
#     def __init__(self):
#
#         self.length = 52
#         self.index = 0
#         self.suits = ['\u2660', '\u2665', '\u2666', '\u2663']
#         self.ranks = [*range(2, 11), 'J', 'Q', 'K', 'A']
#
#     def __lenght(self):
#         return self.length
#
#     def __next__(self):
#
#         if self.index >= self.__lenght():
#             raise StopIteration
#         else:
#             suit = self.suits[self.index // len(self.ranks)]
#             rank = self.ranks[self.index % len(self.ranks)]
#             self.index += 1
#             return f'{rank} of {suit}'
#
#
# a = CardDeck()
#
# try:
#     while True:
#         print(next(a))
# except StopIteration:
#     print('Gengerator has ended.')