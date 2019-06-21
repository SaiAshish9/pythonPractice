# # print('''sai's
# # "project" ''')
# #
# # name = 'abcdefg'
# #
# # n1 = name[:]
# # print(n1)
# # print(f'{n1}= {name}')
# # if name.isupper():
# #     print('ok')
# # else:
# #     print('jo')
# #
# #  #print pattern
# # i=1
# # while i<5:
# #     print('*'*i)
# #     i+=1
# # x="abcef"
# # print(x.split("."))
# # numbers = [5, 2, 5, 7, 1]
# #
# # for x in numbers:
# #     output = ''
# #     for y in range(x):
# #         output += 'x'
# #     print(output)
# #
# # #print max value in a list
# # max = numbers[0]
# # for x in numbers:
# #     if x > max:
# #         max = x
# # print(max)
# #
# # #doubly linked lists
# # matrix=[
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]
# # for x in matrix:
# #     for y in x:
# #         print(y)
# #
# # numbers.append(9)
# # print(numbers[:])
# #
# # #remove duplicates in a list
# # numbers2 = [2,2,2,4,4,6,6]
# # uniques =[]
# # for x in numbers2:
# #     if x not in uniques:
# #         uniques.append(x)
# # print(uniques)
# #
# # phone=input("Number: ")
# # digits = {
# #     "1" :"one",
# #     "2":"two",
# #     "3":"three",
# #     "4":"four",
# #     "5":"five",
# #     "6":"six",
# #     "7":"seven",
# #     "8":"eight",
# #     "9":"nine",
# #     "0":"zero"
# # }
# # output =" "
# # for ch in phone:
# #     output += digits.get(ch,"!" )+" "
# # print(output)
# #
# # message = input(">")
# # words=message.split(' ')
# # emojis ={
# #     ":)" :" 😊",
# #     ":(" : "😌"
# # }
# # output=""
# # for x in words:
# #     output += emojis.get(x,x)+" "
# # print(output)
#
# # try:
# #     age=int(input('Age:'))
# #     age=5/age
# #     print(age)
# # except ValueError:
# #     print('Invalid value')
# # except ZeroDivisionError:
# #     print('ZeroDivisionError')

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("movie")
#     def draw(self):
#         print("draw")
#
# point1= Point(10,20)
# print(point1.x)
# point1.draw()

#
# class Mammal():
#     def walk(self):
#         print("walk")
# class Dog(Mammal):
#     pass
# x=Dog()
# x.walk()
#print(i,end="")
# i=int(input(""))
# y=""
# for x in range(i):
#    y+=str(x)
#    x+=1
# print(int(y))

# from converters import kg_to_lbs
#
# print(kg_to_lbs(0.45))

# import ecommerce.shipping
# ecommerce.shipping.shipping()
#randint(11,20)
# import random
# members=['sai','asd','dsd']
# print(random.choice(members))
# import random
# class Dice():
#     def roll(self):
#         x=random.randint(1,6)
#         y=random.randint(1,6)
#         return x,y
# D=Dice()
# print(D.roll())


