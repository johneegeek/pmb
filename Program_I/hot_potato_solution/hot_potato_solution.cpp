// Programming Merit Badge
// Problem #1 (Using C++)
//
// Using queues, write the 'hot_potato' function
// We will implement a general simulation of Hot Potato. 
// Our program will input an array of names and a constant, call it “num,” to be used for counting. 
// It will return the name of the last person remaining after repetitive counting by num. 

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;  // Without this you need to preface every call with std::



string hot_potato(vector<string> nameList, int num)
{
    // How many items are there?  Need that first.
    int count = nameList.size();
    
    // First we want to push all the values in the list on a queue.
    queue<string> q;
    for (int i=0; i < count; i++)
    {
        q.push(nameList[i]);
    }

    // Now loop through the queue in order 'num' times until there is 
    // one remaining item.
    // (push the item back in the queue before removing it)
    for (int i=0; i < num-1; i++)
    {
        // remove the person from the front and put them in the back.
        q.push(q.front());
        q.pop();
    }

    // return the string name of the 'next' person.   
    return(q.front());
}

int main()
{
    // To make this easier, this was changed from an array of strings
    // to a "vector" of strings.   Very similar, but vector manages
    // it's memory better and will be easier to work with.
    vector<string> s = {"Austin", "Ethan", "Mason", "Matthew", "Zach"};
    
    cout << "Hot potato: `" << hot_potato(s, 2) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 9) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 30) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 42) << '`' << endl;

    return(0);
}

