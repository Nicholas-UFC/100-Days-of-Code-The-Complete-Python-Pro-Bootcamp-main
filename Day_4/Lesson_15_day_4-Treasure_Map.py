# You are going to write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = str(input())  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letra = position[0].lower()
abc = ["a", "b", "c"]
letra_index = abc.index(letra)
numero_index = int(position[1]) - 1
map[numero_index][letra_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
