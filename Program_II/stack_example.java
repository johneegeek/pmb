/**
 * Example of stacks in Java
 */

import java.util.Stack;   // Stacks are in the "util" library

public class stack_example 
{

public static void main(String[] args) 
{
    Stack<Character> stack = new Stack<Character>(); 

    // Push our items on our stack
    for (int i=0; i < 5; i++)
    {
        Character ch = (char)('A' + i);
        System.out.println( "Push: " + ch );
        stack.push(ch);
    }


    // Now take them off of the stack
    while (!stack.empty())
    {
        Character value = stack.pop();
        System.out.println("Pop: " + value);
    }
    
}

    
}