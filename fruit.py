fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "Lime": "a sour green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some fruit please"}

print(veg)

# veg.update(fruit) # adds the fruit to the veg dictionary
# print (veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy() # creates a new dictionary by copying fruit
nice_and_nasty.update(veg) # adds the veg dictionary to thr new nice_and_nasty one with fruit in it already
print(nice_and_nasty)



