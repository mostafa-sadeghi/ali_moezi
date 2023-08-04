# name = input("Enter your name: ")
# family = input("Enter your family: ")
# message = "Hello" + " " + name
# message = "Hello %s %s"%(name, family)
# message = f"Hello {name} {family}"
# print(message)

# print("hello", name, family)


# print("ali " * 5)


# string = "python"
# print(string[0].upper(), end=" ")
# print(string[1].upper(), end=" ")
# print(string[2].upper(), end=" ")
# print(string[3].upper(), end=" ")
# print(string[4].upper(), end=" ")
# print(string[5].upper(), end=" ")
# print(string[0:3])
# print(string[:3])
# print(string[:])
# print(string[2:4])
# print(string[3:6])
# print(string[3:])


# print(string[::2])
# print(string[::-1])

# result = ""
# result += string[0] + " " + string[1] + " "
# print(result)
# result = " ".join(string)
# print(result)


# shopping_list = []
# print(type(shopping_list))
# print(len(shopping_list))
# shopping_list.append("paper")
# shopping_list.append("mashroom")


# print(shopping_list)
# print(len(shopping_list))

# item = input("enter your product's name: ")
# shopping_list.append(item)
# print(shopping_list)
# print(len(shopping_list))

# item = input("enter the product's name for deleteing: ")
# shopping_list.remove(item)
# print(shopping_list)
# print(len(shopping_list))


# numbers = [1,2,3] * 5
# print(numbers)
# print(len(numbers))

# del numbers[14]
# print(numbers)
# print(len(numbers))
# numbers.pop()
# print(numbers)
# print(len(numbers))


# TODO


"""
برنامه ای بنویس که سه عدد از ورودی دربافت نماید و حاصل جمع آنها را نمایش دهد

"""

"""
numbers = [1,2,3,4,5,6,7,8,9]
از لیست بالا برش های زیر را ایجاد نمایید

[1,2,3]
[3,4,5]
[6,7]
[8,9]
[6,7,8,9]

"""


# my_list = ['artin', 1, [11, 22], [[111, 222], [3, 4]]]
# print(my_list)

# TODO

"""
print every items from above list:
artin
1
11
12
111
222
...

"""


my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9]

my_list = my_list1 + my_list2
print(my_list)
my_list = []
my_list.extend(my_list1)
my_list.extend(my_list2)
print(my_list)


my_list = []
my_list.append(my_list1)
my_list.append(my_list2)

print(my_list)
my_list = [my_list1, my_list2]
print(my_list)
