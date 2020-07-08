// Example of how to use a queue in C++

#include <stdio.h>  
#include <queue>

using namespace std;

int main()
{
    int i = 0;
    queue<int> my_queue;

    // "Push" some values onto our queue for later.
    my_queue.push(1);
    my_queue.push(2);
    my_queue.push(3);

    while(!my_queue.empty())
    {
        i = my_queue.front();   // Get the next value from the front of our queue
        my_queue.pop(); // "Pop" the value off of our queue 
        printf("Value = %d\n", i);
    }

    return(0);
}