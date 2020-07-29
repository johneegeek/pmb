import pig as pig
from colorama import Fore as fg
import colorama



def test_set(testtuple):
    s = pig.translate(testtuple[0])
    print('Phrase: `' + testtuple[0] + '`')
    print('Translation: `' + s + '`')
    if s == testtuple[1]:
        print(fg.GREEN + '  CORRECT\n' + fg.RESET )
    else:
        print(fg.RED + '  WRONG, should be: `' + testtuple[1] + '`\n' + fg.RESET)


def main():
    colorama.init()

    tests = [('These are not the droids youre looking for','heseTay reaay otnay hetay roidsday oureyay ookinglay orfay'),
             ('I have a bad feeling about this', 'Iay avehay aay adbay eelingfay boutaay histay'),
             ('Its a trap','tsIay aay raptay'),
             ('Its  against my programming to impersonate a deity ','tsIay  gainstaay ymay rogrammingpay otay mpersonateiay aay eityday ')
             ]
    bonus_tests = [
                  ('Do. Or do not.  There is no try!','oDay. rOay oday otnay.  hereTay siay onay rytay!'),
                  ('Iay maay luentfay niay veroay ixsay illionmay ormsfay foay ommunicationcay!','I am fluent in over six million forms of communication!'),
                  ('ren\'tAay ouyay aay ittlelay hortsay orfay aay tormtrooperSay?','Aren\'t you a little short for a Stormtrooper?'),
                  ('Iay indfay ouryay acklay foay aithfay isturbingday.','I find your lack of faith disturbing.'),
                  ('The Force runs strong in my family. My father has it. I have it. And     my sister has it! ','heTay orceFay unsray trongsay niay ymay amilyfay. yMay atherfay ashay tiay. Iay avehay tiay. ndAay     ymay istersay ashay tiay! '),
                  (' ', ' ')
                  ]


    for test in tests:
        test_set(test)

    print('**** BONUS PHRASES ****\n')
    for bonus in bonus_tests:
        test_set(bonus)



# This checks to see if we are running from the console
# or importing it as a library.
# This way we can run a function (main) when it's run
# by itself.
if __name__ == "__main__":
    main()

