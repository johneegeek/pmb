# For comparison, here is the hot potato program from
# our first problem.

import queue  

def hot_potato(nameList, num):
    q = queue.Queue()

    for i in nameList:
        q.put(i)

    for x in range(1, num):
        q.put(q.get())

    return(q.get())


# Run your function
NList = ["Austin", "Ethan", "Mason", "Matthew", "Zach"]

print('Hot potato: `' + hot_potato(NList, 2) + '`')
print('Hot potato: `' + hot_potato(NList, 9) + '`')
print('Hot potato: `' + hot_potato(NList, 30) + '`')
print('Hot potato: `' + hot_potato(NList, 42) + '`')