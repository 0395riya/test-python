# print(5 ** 2)
# print(5 / 2)
# print(5 % 2)
# print(5 // 2)


# a = int(4.76)
# print(a)


#(in and not in)
# a = 4
# list = [1, 3, 4, 5, 3]
# if(a in list):
#     print("Yes")
# else:
#     print("No")


# Identity Operator
# (is, is not)   example
# x = "Hello World"
# if (type(x) is int):
#     print("Yes")
# else:
#     print("False")


# name = input("Enter Your name:")
# print("Hi ! " + name)


# data = "Python Developer"
# x = len(data)
# print(x)


# data = "Python Developer"
# x = (data.split())
# print(x)


# data = "Python Developer"
# x = (data.center(50))
# print(x)


# isalpha, isdigit, isspace, index, find,  istitle, 

#Join Two tuple  (tuple is collection and immutable)
# hardware = ("monitor", "printer", "mouse", "desktop")
# software = ("photoshop", "java", "react")
# x = hardware + software
# print(x)


# set and dictionaries (set is also a collection which is unordered and unindexed . can't add duplicate item)
#(Dictionaries is a collection which is unordered, changeable and indexed)

# hardware = {"monitor", "printer", "mouse", "desktop"}
# print(hardware)

#(If you want to add multiple item in set)
# hardware = {"monitor", "printer", "mouse", "desktop"}
# hardware.update(["CPU", "RAM", "ROM", "TASK"])
# print(hardware)


# mobile = {
#     "brand" : "Nokia",
#     "model" : "TA-1053",
#     "year" : 2018
# }

# mobile["year"] = 2019
# mobile["color"] = "black"

# # # (delete)
# # mobile.pop("model")
# # #or
# # del mobile["year"]
# # mobile.clear()

# # phone = mobile.copy()
# # print(phone)

# print(mobile)


#Control Flow statements (IF statements) elif, nested-if 

# a = 3
# b = 5
# if (b>a):
#     print("b is greater than a")


# age = int(input("Enter your age :"))
# if age >=18 :
#     print("You are eligible for vote")
# else:
#     print("You are not eligible for vote")


# num = int(input("Enter any number :"))
# if num % 2 == 0 :
#     print("The number is even no.")
# else:
#     print("The number is odd no.")


# while loop

# i = 1
# while i <= 10:
#   print(i)
#   i += 1

#break statement
# i = 1
# while i <= 10:
#   print(i)
#   if i == 4 :
#     break
#   i+= 1


#Continue Statement
# i = 0
# while i < 10:
#   i+= 1
#   if i == 4:
#     continue
#   print(i)


# range() function returns a sequence of numbers, starting from 0 by default, and bydefault increments by 1
# for x in range(7):
#     print(x)

# for x in range(2,7):
#     print(x)


# Functions in Python (A function is block of code that performs aspecific task.)
# (Built in function)
# a = 2
# b = 3
# c = max((a, b))
# print(c)

# (User define function)
# a = 2
# def my_data():
#     b = a*a
#     print(b)
# my_data()


# def percentage(total):
#     per = (total / 500)*100
#     return per
# phy = 86
# eng = 56
# math = 89
# hindi = 76
# total = sum((phy,eng,math,hindi))
# result = percentage(total)
# print("Your total number is:", total)
# print("Your percentage is :", round(result,2))


# (Lambda Function - One line funtion or anonymous function)

# def sqrt(a):
#     print(a*a)
# sqrt(4)   

# sqt = lambda a : a*a 
# print(sqt((5)))


# (Modules - A modules is a file containing function which can be imported and used in our programs )


### -----------------------------------------------------------------


import time;
import calendar;

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

#or
# localtime = time.asctime()
# print(localtime)

# cal = calendar.month(2025, 8)
# print(cal)


# import mymodule;

# data = mymodule.cube(4)
# print(data)


# Two type of file (1. Text file (.txt)   2. Binary files (.jpg, .dat))

## Opening a file     "r"- mode
# open("file_name.txt", "r")

## Reading a file
# f = open("Test.txt", "r")
# myfile = f.read()
# print(myfile)
# f.close()


#  