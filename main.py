import random

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'y', 'x', 'z']
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'Y', 'X', 'Z']
num = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!','@', '#', '$', '%', '^', '&', '*', '<', '>']
all = small + big + num + special

x = int(input())

for k in range(x + 1):
    password = random.choice(all)
    print(password, end="")