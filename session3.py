# numbers = (1,2,3,4,5,6,7,8,9)
# print(type(numbers))

# numbers[0] = 100 # error
# print(numbers[0])
# print(len(numbers))
# print(numbers[:3])

from turtle import Screen, Turtle, done
favorite_sports = {
    'sara': 'football',
    'artin': 'baseball',
    'armin': 'tennis'
}

# print(f"sara likes {favorite_sports['sara']}")
# print(f"artin likes {favorite_sports['artin']}")
# print(f"armin likes {favorite_sports['armin']}")

# new_person = input("enter a name: ")
# fav_sport = input("enter a sport: ")

# favorite_sports[new_person] = fav_sport

# print(favorite_sports)

# del favorite_sports['armin']
# print(favorite_sports)

# TODO
"""
برنامه ای بنویس که نام، نام خانوادگی، سن و معدل سه دانش آموز را از ورودی دریافت می نماید و در لیستی ذخیره می نماید
برنامه قابلیت تغییر اطلاعات دانش آموزان را دارد
به این صورت که امکان حذف و نیز ویرایش سن و معدل دانش آموزان وجود دارد
"""


main_surface = Screen()
main_surface.bgcolor("cyan")
main_surface.title("Hello")
main_surface.setup(600, 600)

my_turtle = Turtle()
my_turtle.forward(100)
my_turtle.left(120)

# TODO  کشیدن مربع، مثلث و ....


done()
