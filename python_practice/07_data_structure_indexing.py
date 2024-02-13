# DATA STRUCTURES

# 1 - list (It is very important in data science)
food = ["Dahi Bhalay", "Biryani", "Daal", "Samosay", "Shami", "Palak Paneer"]
print(food)
print(food[1])
print(food[-1]) # -1 displaying list in reverse order

food[1] = "Chicken Polao" # Update the item of list
print(food)

# 2 - tuple (Tuple item can be update)
coordinates = (1, 2.2, 3.1, 2.5)
print(coordinates)
print(coordinates[0])

# 3 - Sets
fruit_set = {"Dahi Bhalay", "Biryani", "Daal", "Samosay", "Shami", "Palak Paneer"}
print(fruit_set)
fruit_set.add('Pakora') # To add more items in a set
print(fruit_set)

# 4 - Dictionary
car = {"brand": "Ford", "model": "Mastang", "year": 1964}
print(car)
print(car["model"])
car["year"] = 2023 # To update the items of dictionary
print(car)
