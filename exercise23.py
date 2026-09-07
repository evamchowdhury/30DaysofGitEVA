str = 'You cannot end a sentence with because because because is a conjunction'
print(str.find('because'))
print(str.rfind('because'))
new = (str.replace("because", "")).strip()
print(" ".join(new.split()))

print('   Coding For All      '.strip())
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
nlist = " #".join(list)
print("#", nlist)

print("""I am enjoying this challenge. 
I just wonder what is next.""")

print("""Name\tAge\tCountry\tCity\nAsabeneh 250\tFinland\tHelsinki""")

#35
radius = 10 
area = 3.14 * radius**2. 
print(f"The area of a circle with radius {radius} is {area} meters square.")

a = 8
b = 6
add = a + b
subtract = a - b
multiplication = a*b
division = "{:.2f}".format(a/b)
modulus = a%b
floor = a//b
exponent = a**b

print(add, subtract, multiplication, division, modulus, floor, exponent, sep="\n")