# def text_reader(filename: str) -> list:
#     with open(filename) as file:
#         data = file.read().split('\n')
#     return data

'''Actual generator'''
# def text_reader(filename: str) -> list:
#     for row in open(filename):
#         yield row
#
# text = text_reader('datafile.txt')
#
# row = next(text)
#
# # print(row)
# while row:=next(text):
#     print(row, end='')

'''Infinet sequence'''
# def infinet_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
# t = infinet_sequence()
#
# while True:
#     print(next(t))

'''is_palindrom'''
# def is_palindrom(num):
#     if num // 10 == 0: # Skip single digit inputs
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return num
#     else:
#         return False

'''Infinet + is_palindrom'''
# for i in infinet_sequence():
#     pal = is_palindrom(i)
#     if pal:
#         print(pal)



