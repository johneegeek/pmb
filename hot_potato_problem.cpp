// Programming Merit Badge
// Problem #1 (Using C++)
//
// Using queues, write the 'hot_potato' function
// We will implement a general simulation of Hot Potato. 
// Our program will input an array of names and a constant, call it “num,” to be used for counting. 
// It will return the name of the last person remaining after repetitive counting by num. 

#include <iostream>
#include <string>
#include <queue>

using namespace std;  // Without this you need to preface every call with std::



string hot_potato(string nameList[], int num)
{
    // First we want to push all the values in the list on a queue.
    
    //TODO:  Your code here.


    // Now loop through the queue in order 'num' times until there is 
    // one remaining item.
    // (push the item back in the queue before removing it)


    // return the string name of the 'next' person.   
}

int main()
{
    string s[] = {"Austin", "Ethan", "Mason", "Matthew", "Zach"};

    cout << "Hot potato: `" << hot_potato(s, 2) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 9) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 30) << '`' << endl;
    cout << "Hot potato: `" << hot_potato(s, 42) << '`' << endl;

    return(0);
}

