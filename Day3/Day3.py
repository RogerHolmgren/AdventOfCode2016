#!/usr/bin/python
def is_triangle(a,b,c):
    return (a+b>c) and (a+c>b) and (c+b>a)

# Start of program
possible = []
total = []
f = open('input.txt', 'r')
#f = ["5 10 25","4 4 24"]
for line in f:
    t = line.split()
    if is_triangle(int(t[0]),int(t[1]),int(t[2])) :
        possible.append(t)
    total.append(t)
f.close()
print("Valid triangles: {}".format(len(possible)))
print("Total inputs : {}".format(len(total)))


