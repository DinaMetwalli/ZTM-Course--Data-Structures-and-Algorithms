# Linear Time Complexity Exercise.

import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['dory' for i in range(999999)]
large.append('nemo')

def find_nemo(array) -> None:
    startTime = time.time()
    for item in array:
        if item == "nemo":
            print("Found nemo!")
            # break
    endTime = time.time()
    print(f'The search took {endTime - startTime} seconds.\n')

find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)

#----------------------------------------------------------------

def funchallenge(input):
    startTime = time.time()
    temp = 10 #O(1)
    temp = temp +50 #O(1)
    for i in range(len(input)): #O(n)
        var = True #n*O(1)
        a += 1 #n*O(1)
    endTime = time.time()
    print(f'The search took {endTime - startTime} seconds.\n')
    return a #O(1)

funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)

# O(1 + 1 + 1) + O(n*1 + n*1 + n*1) = O(3 + 3n) = O(3(n+1)) -> O(n)