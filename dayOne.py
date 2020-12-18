import numpy as numpy

data = numpy.loadtxt("dayOne.txt")

count = 0

for a in data:
    for b in data:
        #print(count, '- Adding', a, '+', b, ':', (a+b))
        count += 1
        if (a+b) == 2020:
            #print("FOUND!")
            print(a, '+', b, '=', a+b)
            print(a, 'x', b, '=', a*b) # Answer is produced here
