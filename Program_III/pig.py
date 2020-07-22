# Pig latin Translator
# Be able to translate from English to Pig Latin
# (and for a bonus, translate the other way)
#
#
import string
import re
import argparse
import sys


# EnglishToPig function
# 
# Given a passed in "English" string, return
# the string converted to Pig Latin.
#
# English is translated to pig latin by taking the first
# letter of every word, moving to the end of the word, and adding 'ay'
#
# (BONUS if you can handle punctuation.)
#
def EnglishToPig(str):
    """
    Given a string 'str' convert it from English to Pig Latin
    """

    # TODO:  Your code here


    # Change the return to return the converted string
    return("")


# BONUS FUNCTION
# (optional)
#
# Given a string in Pig Latin, return the string converted to English
#
def PigToEnglish(str):
    """
    Given a string 'str' convert it from Pig Latin to English
    """

    # TODO:  Your code here


    # Change the return to return the converted string
    return("")





###############################################################################
# 
# Don't modify below this
# 
###############################################################################

def isPig(str):
    """
    Test a given string and determine if it is Pig Latin.
    This is advanced.
    """
    _pigpat = re.compile(r'.ay(\s|[?.])')
    # If we find more than one pig pattern we'll assume it's Pig Latin
    # This won't work when there are words like say or hay in the
    # text, but this is good for our purposes.
    return(bool( len(_pigpat.findall(str)) >= 2 ))
    

def translate(str):
    """
    Combined function to translate to and from Pig Latin
    """
    if isPig(str):
        return(PigToEnglish(str))
    return(EnglishToPig(str))


def main():
    """
    A kind of "Main" program that we can run to test out our
    functions
    """
    parser = argparse.ArgumentParser(prog='pig', 
                                     description="English to Pig Latin translator",
                                     epilog='(lsoAay aay igPay atinLay otay nglishEay ranslatortay!)')
    parser.add_argument('text', nargs='?')
    args = parser.parse_args()

    if not args.text:
        # No text was given on the command line, so we will 
        # translate our test messages.
        phrases = ['These are not the droids youre looking for', 
                   'I have a bad feeling about this']
        bonus_phrases = ['Do. Or do not.  There is no try!',
                         'Iay maay luentfay niay veroay ixsay illionmay ormsfay foay ommunicationcay!',
                         'ren\'tAay ouyay aay ittlelay hortsay orfay aay tormtrooperSay?',
                         'Iay indfay ouryay acklay foay aithfay isturbingday.']

        for phrase in phrases:
            print('\nOriginal phrase: ' + phrase )
            print('Translation:     ' + translate(phrase))

        print('\n**BONUS PHRASES**')
        for phrase in bonus_phrases:
            print('\nOriginal phrase: ' + phrase )
            print('Translation:     ' + translate(phrase))
        sys.exit(0)

    # Text was given on the command line.  Translate it.
    print(translate(args.text))

#------(end of main)-----------------------------------------------------------



# This checks to see if we are running from the console 
# or importing it as a library.
# This way we can run a function (main) when it's run
# by itself.
if __name__ == "__main__":
    main()


