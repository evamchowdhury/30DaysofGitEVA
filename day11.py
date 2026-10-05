def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

def area_of_circle(radius):
    area = radius * radius * 3.14
    return area

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def check_season(month):
    seasons = {"Autumn": ["September", "October", "November"],
     "Winter": ["December", "January", "Febuary"],
     "Spring": ["March", "April", "May"],
     "Summer": ["June", "July", "August"]
     }
    for season_name, months_list in seasons.item():
        if month in months_list:
            return season_name

    return "Unknown"

import math

def solve_quadratic(a, b, c):
    x_one = (-1 * b + math.sqrt(b**2 - (4*a*c)))/(2*a)
    x_two = (-1 * b - math.sqrt(b**2 - (4*a*c)))/(2*a)
    return x_one, x_two

def print_list(list):
    print(list)


def print_reversed(list):
    for word in reversed(list):
        print(word, end=", ")

print_reversed([1, 2, 3, 4,])
fruits = ['banana', 'pear', 'apple']
def print_capitalized(list):
    for word in list:
        print(word.upper(), end=", ")

print_capitalized(fruits)


def add_item(list, addition):
    list.append(addition)
    print(list)

add_item(fruits, "cherry")

def remove_item(list, remove):
    list.remove(remove)
    print(list)

remove_item(fruits, "pear")