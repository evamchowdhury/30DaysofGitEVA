dog = {}
dog = {
    "name":"dog",
    "color":"black",
    "breed":"bull dog",
    "legs":4,
    "age":3
}

student={
    "firstname":"Eva",
    "lastname": "iscool",
    "gender": "female",
    "age": "14",
    "marital status": "single",
    "skills": ["Drawing", "Python"],
    "country": "Canada",
    "address":{
        "city": "Toronto", 
        "street": "Space Avenue", 
}
}
print(len(student))
print(student["skills"])
student["skills"].append("studying")
print(student["skills"])
print(student.keys())
print(student.items())
del student['marital status']
del student
