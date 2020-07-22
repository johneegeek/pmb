# Our reverse string problem in Python

import queue

def reverse(str):
    stack = queue.LifoQueue()

    for x in str:
        stack.put(x)

    s = ''
    while not stack.empty():
        s += stack.get()
        
    return(s)

# Run your function
BackwardsStr = ".desrever neeb evah I"
print(reverse(BackwardsStr))

