# Conditional statements
x = 10
if x == 10:
    print("x is equal to 10")
elif x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
else:
    print("x is zero")

# for Loop
menu = ["Dahi Bhalay", "Biryani", "Daal", "Samosay", "Shami", "Palak Paneer"]
for food in menu:
    print(food)

# while loop
i = 1
while i < 6:
    print(i)
    i = i+1

# for loop example-1
for letters in "Python":
    if letters == 'h':
        break  # This statement will the break the loop when if condition is become true
    print(letters)

# for loop example-2
for letters in "Python":
    if letters == 'h':
        continue  # This statement will the continue the loop from letter 'h' to onward
    print(letters)

# for loop example-3
for letters in "Python":
    if letters == 'h':
        pass  # This statement will print all characters to by-pass the if condition
    print(letters)