# Understanding the loops and nested loops
# Also understanding how it affects the time complexity of the algorithm

import time 

start_time = time.strftime("%H:%M:%S")
print(" START TIME : " + start_time)
for i in range(10):
    for j in range(i):
        print("*" , end=" ")
    print("")
end_time = time.strftime("%H:%M:%S")
print(" END TIME : " + end_time)