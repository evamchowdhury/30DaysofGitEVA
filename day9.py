user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are old enough to drive")
else:
    left = 18 - user_age
    print(f"You need {left} more years to learn to drive")

my_age = 14
difference = user_age - 14
if difference > 0:
    print(f'You are {difference} years older than me')
elif difference < 0:
    print(f"You are {abs(difference)} years younger than me")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal than {b}")


grade = int(input("What is your grade? "))

if 90<grade<100:
    print("A")
elif 80<grade<89:
    print("B")
elif 70<grade<79:
    print('C')
elif 60<grade<69:
    print('D')
elif 0<grade<59:
    print("F")

month = input("enter month: ")
fall = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in fall:
    print("its fall")
elif month in spring:
    print("its spring")
elif month in winter:
    print("its winter")
elif month in summer:
    print("its summer")


fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter fruit: ")
if user_fruit not in fruits:
    fruits.append(user_fruit)
    print(fruits)
else: 
    print("That fruit already exist in list")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person:
    print(person["skills"][3])
    if "Python" in person["skills"]:
        print("Y")
    elif ["Javascript", "React"] in person["skills"]:
        print('He is a frot end developer')
    elif ["Node", "Python", "MongoDB"] in person["skills"]:
        print('He is a backend developer')
    elif ["React", "Node", "MongoDB"] in person["skills"]:
        print("He is a fullstack developer")

if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person["first_name"]} {person["last_name"]} lives in Finland. He is married")

