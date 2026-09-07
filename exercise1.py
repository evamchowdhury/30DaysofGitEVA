#exercise 1
string = ['Thirty', 'Days', 'Of', 'Python']
string = " ".join(string)
print(string)

#exercise 2
strin = ['Coding', 'For' , 'All']
strin = " ".join(strin)
print(str)

#exercise 3
stri = "Coding For All"
stri = stri.split()
print(stri)
print(len(stri))
stri = " ".join(stri)
print(stri.upper())
print(stri.lower())

#exercise 8
print(stri.title())
slice = stri[:6]
print(slice)
found = stri.find("Coding")
print(found)

#exercise 11
new = stri.replace("Coding", "Python")
new = stri.replace("All", "Everyone")
stri.split(" ")
print(stri)

print(stri[0])
print(stri[-1])
print(stri[10])

#exercise 18
words = stri.split()
acronym = "".join(word[0].upper() for word in words)
print(acronym)

print(stri.index("C"))
print(stri.rfind("l"))