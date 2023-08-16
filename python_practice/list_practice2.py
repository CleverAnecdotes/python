temperatures = ["monday", 98, 36.5]
rainfall = ["hawaii", 38, 22.5, temperatures, [3, 5, 7]]

print(rainfall[3:])
print(rainfall[:4])
print(temperatures[:2])
print(rainfall[-2])
# Remember that calling up part of a list never calls the number you list as the final
# For example :3 will not call the third position, but the second. It stops at the third.