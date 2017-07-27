#place to figure shit out
import time
from collections import deque


#which reverse has better performance

#setup
arr= list(range(0,10000000))

start_time = time.time()
reversed(arr)
end_time=time.time()
print("Array reversed: ", end_time)
start_time=time.time()
deque(arr).reverse()
end_time=time.time()
print("Deque reversed: ", end_time)
