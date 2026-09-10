empty = ()
brothers = ("jimmy", "john", "johnny")
sisters = ("sam", "sarah")
siblings = brothers + sisters
print(f"You have {len(siblings)} siblings.")
parents = ("Dad", "Mom")
family = siblings + parents
brother, brother1, brother2, sister, sister1, dad, mom = family
#lvl 2
fruits = ("banana", "apple", "orange")
vegetables = ("carrot", "broccoli", "cabbage")
animal = ("beef", "chicken", "milk")
food = fruits + vegetables + animal
food_list = list(food)
print(food_list)
three = food[5]
del food
print(three)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
Estonia = "Estonia" in nordic_countries
Iceland = "Iceland" in nordic_countries
print(Estonia, Iceland)