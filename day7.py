it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Dell", "LG", "Aseus"])
it_companies.remove("Facebook")
#remove will return ERROR if item doesnt exist, discard will not

AB = A.union(B)
intercept = A.intersection(B)
print(intercept)
print(A.issubset(B))
print(A.isdisjoint(B))

BA = B.union(A)
sym = B.symmetric_difference(A)
print(sym)

age_set = set(age)
print(len(age), len(set))
#str: made with "", 1 value
#list: multiple values together, ordered, changable, []
#set: unordered, values are all unique {}
#tuple: ordered sequences; cannot be changed

str = "I am a teacher and I love to inspire and teach people."
str_list = text(str)
str_set = set(str_list)

half_set = len(str_list)//2
set_a = set(str_list[:half_set])
set_b = set(str_list[half_set:])
dif = set_b.symmetric_difference(set_a)
print(dif)