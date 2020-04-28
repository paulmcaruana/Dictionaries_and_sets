# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set({"lion", "tiger", "panther", "elephant", "hare"})
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
# empty_set = set()
# empty_set_2 = {} # this creates a dictionary not a set so can't be used
# empty_set.add("a")
# # empty_set_2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("=" * 40)
#
# # the below will print out the numbers in even and squares that appear in both
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
# # the three blocks above print out:
#
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# [4, 6, 9, 16, 25]
# even minus squares
# [0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# [0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# squares minus even
# {9, 25}
# {9, 25}
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
# The above code prints the following...
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# {4, 6, 9, 16, 25}
# [0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# this prints out....(everything other than the ones that are in both)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# [4, 6, 9, 16, 25]
# symmetric even minus squares
# [0, 2, 8, 9, 10, 12, 14, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38]
# symmetric squares minus even
# [0, 2, 8, 9, 10, 12, 14, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38]

# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error, does nothing
# print(squares)
# # squares.remove(8) # generates error because the item is not in the set. Should do the following instead
#
# # if 8 in squares:
# #     squares.remove(8)
#
# #alternatively you could use exception handling
#
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))

print(even)
even.add(3) # thrwos an error as you can't add to a frozen set as it is immutable

