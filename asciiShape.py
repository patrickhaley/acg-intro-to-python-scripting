# This code prints a diamond shape using astrisks
# The user can change the value of length to change the size of the diamond
length = 7
astr = "*"
for i in range(length):
  for j in range(length-i):
    print(" ", end='')
  print(astr)
  astr += "**"

length -= 1
space = 1
astrNum = ((length*2)-1)
astr = "*" * astrNum
for i in range(length):
  print(" " + space * " " + astr)
  astrNum -= 2
  astr = "*" * astrNum
  space += 1