import numpy as numpy

data = numpy.genfromtxt('input.txt', dtype='str')
validPasses = 0

for test in data:
    print(test)
    #[0] is required #
    #[1] is required letter plus :
    #[2] is given password

    times = test[0].split('-')
    #print(times)
    for i in range(0, len(times)):
        times[i] = int(times[i])
    print(times)
    low = times[0]
    high = times[1]

    letter = test[1].split(':') # split into letter and colon
    letter = letter[0] # drop colon
    print(letter)

    passwd = test[2]

    count = passwd.count(letter)
    print(count)
    if (count >= low) and (count <= high):
        print("Valid")
        validPasses += 1
print(validPasses) # ANSWER