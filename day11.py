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

def sum_of_numbers(numbers):
    total =+ numbers
    print(total)

print(sum_of_numbers(10))

def sum_of_evenodds(numbers):
    odds = []
    evens = []
    for n in range(n, n +1):
        if n % 2 !=0:
            odds.append
        else:
            evens.append

    totalo = sum(odds)
    totale = sum(evens)
    
    return totalo, totale

print(sum_of_evenodds(10))

def sum_of_evenodds(numbers):
    odds = []
    evens = []
    for n in range(0, numbers + 1):
        if n % 2 !=0:
            odds.append(n)
        else:
            evens.append(n)

    totalo = len(odds)
    totale = len(evens)
    
    return totalo, totale

print(sum_of_evenodds(100))

def sum_of_evenodds(numbers):
    odds = []
    evens = []
    for n in range(0, numbers + 1):
        if n % 2 !=0:
            odds.append(n)
        else:
            evens.append(n)

    totalo = sum(odds)
    totale = sum(evens)
    
    return totalo, totale

print(sum_of_evenodds(100))


def evens_odds(numbers):
    odds = []
    evens = []
    for n in range(0, numbers + 1):
        if n % 2 !=0:
            odds.append(n)
        else:
            evens.append(n)

    totalo = len(odds)
    totale = len(evens)
    
    return totalo, totale


print(f"evens, odds {evens_odds(10)}")


def factorial(number):
    total = 1
    for n in range(1, number +1):
        total *= n
    return total

print(factorial(5))


def is_empty(value):
    if not value:
        return True
    else:
        return False
    
    
print(is_empty("hello"))
print(is_empty([]))


def calculate_mean(list):
    list.sort()
    length = len(list)
    mean = sum(list)/len(list)
    return mean
    
    
print(calculate_mean(numbers))


def calculate_median(list):
    list = sorted(list)
    length = len(list)
    pos = int(length/2)
    median = list[pos]
    return median

print(calculate_median(numbers2))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
numbers2 = [23, 1, 42, 15, 28]

def calculate_range(list):
    list = sorted(list)
    min = list[0]
    max = list[-1]
    range = max - min
    return range

print(calculate_range(numbers2))

def greet(name=None):
    if not name:
        print("Hello, Guest")
    else:
        print(f"Hello, {name}")
        
        
greet()
greet("Alice")

def show_args(name, age, city):
    print(f"name: {name} age:{age}, city{city}")
    
show_args(name="Alice", age=30, city="New York")