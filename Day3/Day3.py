#!/usr/bin/python

myList = []
f = open('input.txt', 'r')
#f = ["5 10 25","4 4 24"]
for line in f:
    t = line.split()
    print(t)
    if int(t[0]) + int(t[1]) > int(t[2]) :
        if int(t[0]) + int(t[2]) > int(t[1]) :
            if int(t[2]) + int(t[1]) > int(t[0]) :
                myList.append(t)
f.close()
print ("Valid triangles: {}".format(len(myList)))


