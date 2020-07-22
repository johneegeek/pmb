/**
 *   Problem #2 using Java
 *       - Write a function that takes a string and
 *       - reverses
 */
import java.util.Stack;   // Stacks are in the "util" library


public class ReverseStringSolution 
{

    // Given a string, reverse all the characters
    // 
    public static String reverse(String str)
    {
        // Create a stack to store the characters of the string
        Stack<Character> char_stack = new Stack<Character>(); 

        // Go through the characters of the string and push
        // each character on the stack.
        // using simple for loop
        for (int i = 0; i < str.length(); i++) 
        {
            char_stack.push( str.charAt(i) );
		}

        // Create a new string to return
        // Go through the stack and "pop" off the characters and 
        // put them on a string.
        String NewString = "";

        while (!char_stack.empty())
        {
            Character ch = char_stack.pop();
            NewString += ch;
        }

        // Return the reversed string.
        return( NewString );

    }



    public static void main (String[] args)
	{
        String str = ".desrever neeb evah I";

		str = reverse(str);
		System.out.println(str);
	}
    
}