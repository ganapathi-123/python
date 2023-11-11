# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
line1 = ["⬜","⬜","⬜"]
line2 = ["⬜","⬜","⬜"]
line3 = ["⬜","⬜","⬜"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
#print(f"position is {position}")
A1 = map[0][0]
A2 = map[1][0]
A3 = map[2][0]
B1 = map[0][1]
B2 = map[1][1]
B3 = map[2][0]
C1 = map[0][2]
C2 = map[1][2]
C3 = map[2][2]

line1 = [A1,B1,C1]
line2 = [A2,B2,C2]
line3 = [A3,B3,C3]

if (position == "A1"):
  line1[0] = "X"
elif(position== "B1"):
  line1[1] = "X"
elif(position == "C1"):
  line1[2] = "X"
elif(position == "A2"):
  line2[0] = "X"
elif(position == "B2"):
  line2[1] = "X"
elif(position == "C2"):
  line2[2] = "X"
elif(position == "A3"):
  line3[0] = "X"
elif(position == "B3"):
  line3[1] = "X"
elif(position == "A3"):
  line3[2] = "X"
#print(line2[2])

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")