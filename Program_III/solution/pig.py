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
    # To make this easier, convert the string to a list of strings
    # so each word is separated.
    word_list = str.split(' ')
    pig_list = []
    for word in word_list:
        # Take the first letter and add "ay" and move it to the end of
        # the word.

        # Strip off any extra whitespace
        # If there are extra spaces in the input
        # this will fix it.
        cleanword = word.strip()
        
        # BONUS: There could be the possibility that someone punctuated the sentence.
        # which would mean the end of some words could have punctuation on them.
        if cleanword:
            punct = ''
            if cleanword[-1] in string.punctuation:
                punct = cleanword[-1]
                cleanword = cleanword[:-1]

            # Translate to pig
            suffix = cleanword[0] + 'ay'
            new_word = cleanword[1:] + suffix + punct
            pig_list.append(new_word)
        else:
            # We're ignoring this, just use it as is.
            # (things like spaces)
            pig_list.append(word)

    # Convert back to a string and return
    return(' '.join(pig_list))


# BONUS FUNCTION
# (optional)
#
# Given a string in Pig Latin, return the string converted to English
#
def PigToEnglish(str):
    # To make this easier, convert the string to a list of strings
    # so each word is separated.
    word_list = str.split(' ')
    eng_list = []

    for word in word_list:
        cleanword = word.strip()

        if cleanword:
            punct = ''
            if cleanword[-1] in string.punctuation:
                punct = cleanword[-1]
                cleanword = cleanword[:-1]
        
            if len(cleanword) < 3:
                eng_list.append(word)
                continue

            # Translate to English
            if cleanword[-2:] == 'ay':
                new_word = cleanword[-3] + cleanword[:-3] + punct
                eng_list.append(new_word)
            else:
                # Not Pig, ignore and put back the way it is.
                eng_list.append(cleanword)
        else:
            # We're ignoring this, just use it as is.
            # (things like spaces)
            eng_list.append(word)

    # Convert back to a string and return
    return(' '.join(eng_list))



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
    _pigpat = re.compile(r'(\S*ay)\s*[?.!,]?')

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


