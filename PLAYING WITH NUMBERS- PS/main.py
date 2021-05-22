import sys, time, os

# 1
a = list(range(1, 26, 1))
print(a, '26 ', end='')
b = list(range(25, 0, -1))
print(b)
# /1

##2(INTRODUCTION STARTS HERE)
width = 180
print('', 1, ''.rjust(width), '', 1, '')
print('', 2, '|HELLO|'.center(width), '', 2, '', end='\n')
print('', 3, 'WELCOME TO THE WORLD OF NUMBERS '.center(width), '', 3, '')
print('', 4, ''.rjust(width), '', 4, '')
msg = " 5"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
msg = "INTRODUCTION:".center(width)
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
msg = "   5\n"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
##/2

###3
width = 180
msg = " 6"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
msg = "THIS IS THE PLACE WHERE YOU CAN PLAY WITH NUMBERS,WITH THEIR PATTERNS AND ALSO CAN EXPLORE THE TYPES OF NUMBER SYSTEM :)".center(width)  # IMPORTANT***
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
msg = "   6\n"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print('', 7, ''.rjust(width), '', 7, '')
###/3(INTRODUCTION ENDS HERE)

####4 Q/A
width = 180
print('', 7, ''.rjust(width), '', 7, '')
print('', 8, 'NOW BEFORE WE GET STARTED: LETS TEST YOUR KNOWLEDGE ABOUT NUMBERS!'.center(width), '', 8, '', end='\n')
print('', 9, 'SOLVE THIS EQUATION WITH LOGIC:IF YOU GET IT RIGHT YOU WILL GET DIRECTLY LOGGED IN:'.center(width), '', 9,'')
print('', 10, ''.rjust(width), '', 10, '')
print('', 11,'Q. "√-1.2^3.Σπ" and it was delicious!(translate the quoted region in english to complete the sentence)'.center(width), '', 11, '')
print('', 12, 'OR DO YOU WANT TO CHANGE UP THE QUESTION?(yes or no)'.center(width), '', 12, '')
width = 92
E = (input(" ".center(width)))

#QUESTION 2 STARTS ON ANSWERING YES ABOVE'''#question 2
if E == 'yes':
    width = 180
    print('', 13, 'OK SO HERE IS ANOTHER ONE FOR YOU:'.center(width), '', 13, '')
    print('', 14, ''.rjust(width), '', 14, '')
    print('', 15, 'Q. "Divide 20 by half and add 30", what do you get?'.center(width), '', 15, '')
    print('', 16, ' ANSWER:-'.center(width), '', 16, '')
    print('', 17, ''.rjust(width), '', 17, '')
    width = 92
    A = (input(" ".center(width)))
    width = 180

    '''WHEN THE ANSWER IS CORRECT (70)'''
    if A == '70':
        print('', 18, ''.rjust(width), '', 18, '')
        print('', 19, 'YOU GOT SOME CHILLS...HUHH!'.center(width), '', 19, '')
        print('', 20, '|YOU ARE SUCCESSFULLY LOGGED IN|'.center(width), '', 20, '')

        # MAIN TOPIC STARTS FROM HERE I.E. WHAT TO DO WITH NUMBERS

        print('', 21, ''.rjust(width), '', 21, '')
        print('', 22, 'NOW SELECT WHAT DO YOU WANT TO DO WITH NUMBERS'.center(width), '', 22, '')
        print('', 23, 'PLAY WITH NUMBERS(PRESS 1)'.ljust(width), '', 23, '')
        print('', 24, 'OR'.center(width), '', 24, '')
        print('', 25, 'FIND OUT VARIOUS NUMBER SEQUENCE(PRESS 2)'.rjust(width), '', 25, '')
        width = 93
        WHATTODO = (input(" ".center(width)))

        # PLAY WITH NUMBERS LOOP START FROM HERE WITH 2 CHOICES

        #SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 1)
        if WHATTODO == '1':
            width = 180
            print('', 26, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 26, '')

            # 1st choice

            msg = " 27"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "   27\n"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)

            # 2nd choice

            msg = " 28"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "   28\n"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)

            print('', 29, ''.rjust(width), '', 29, '')

            width = 92
            CHOICE = (input(" ".center(width)))

            #SELECTING FROM VARIOUS CHOICES GIVEN
            if CHOICE == '1':

                #ALLEN ASSISTANT


                width=180
                print('', 30, ''.rjust(width), '', 30, '')
                print('', 31,'WELCOME TO MAGICA'.center(width), '', 31, '')
                print('', 32, ''.rjust(width), '', 32, '')
                print('', 33, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 33, '')
                print('', 34, ''.rjust(width), '', 34, '')

                width=173
                msg = " 35"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print(' ALLEN-',end='')
                msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   35\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                msg = " 36"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print(' ALLEN-', end='')
                msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   36\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                #ALLEN USER TALK:-
                print()
                USER = (input("      YOU-"))                                        # ALLEN USER TALK 1
                print()
                # /ALLEN USER TALK:-

                #WHEN USER SAID YES
                if USER =='yes':                                                                                         # when user said yes to allen

                    msg = " 37"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   37\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    #ALLEN 3 DOTS

                    msg = " 38"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print(' ALLEN-', end='')
                    msg = "......".ljust(width)  # A 4TH LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   38\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1) #

                    msg = " 39"                                            #ALLEN CONTINUES TO TALK
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   39\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)



                    #NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                    msg = " 40"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(width)  # A 6TH LINE AND STEP 1
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   40\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 41"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(width)       # A 7TH LINE AND STEP 2
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   41\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 42"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(width)  # A 8TH LINE AND STEP 3
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   42\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 43"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   43\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(width)  # A 10TH LINE AND STEP 5
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(width)  # A 11TH LINE AND PART OF STEP 5
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 46"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(width)  # A 12TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    msg = "   46\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 47"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(width)  # A 13TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    msg = "   47\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # ALLEN USER TALK:-
                    print()
                    USER_ANS = int(input("    YOUR ANS-"))
                    USER_ANS2 = int(input("    YOUR YOB-"))                                                              #ALLEN USER TALK 2
                    DIFF= USER_ANS-USER_ANS2
                    AGE= DIFF%100
                    CHOOSEN_NO=DIFF//100
                    print()
                    # /ALLEN USER TALK:-

                    msg = " 48"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print(' ALLEN-', end='')
                    msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust( width)  # A 14TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   48\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)

                    print()
                    print('    ALLEN- ', end='')
                    print("SO YOUR AGE IS: ",end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                    print(AGE,"YEARS")

                    print('    ALLEN- ', end='')
                    print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",end='') # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                    print(CHOOSEN_NO)
                    print()

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 49, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 49, '')
                    print()
                    width = 93
                    A_C2 = (input(" ".center(width)))
                    print()
                    if A_C2 == 'yes':
                        width = 180
                        print('', 50, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 50, '')
                        print()
                        print('', 51, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 51, '')
                        width = 95
                        print('', 52, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 52, '')
                        width = 180
                        print('', 53, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 53, '')
                        width = 300
                        print('', 54,
                              'COMPOSITE NUMBERS(PRESS 4)                                         54'.center(width))
                        width = 180
                        print('', 55, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 55, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 56, '---EVEN NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 56, '---ODD NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 56, '---PRIME NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 56, '---COMPOSITE NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 56, '---FIBONACCHI NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57,
                                  'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                        '''END OF WHATTODO=2'''

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 58"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   58\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(59, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif A_C2 == 'no':
                        width = 180
                        print()
                        print('', 49, 'OK BYE'.center(width), '', 49, '')
                        print('', 50, 'ENJOY YOUR DAY :)'.center(width), '', 50, '')
                        for i in range(51, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''MAGIC YES FINALLY FINISHED'''

                #WHEN USER SAID NO
                elif USER =='no':                                                                                       # when user said no to allen


                     msg = " 37"
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                     print(' ALLEN-', end='')
                     msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                     msg = "   37\n"
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                     msg = " 38"
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                     print(' ALLEN-', end='')
                     msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                     msg = "   38\n"
                     for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                     #OFFERING 2ND CHOICE TO USER.................................
                     width = 180
                     print('', 39, ''.rjust(width), '', 39, '')
                     print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                     print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                     print('', 42, ''.rjust(width), '', 42, '')
                     print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                     print('', 44, ''.rjust(width), '', 44, '')
                     print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                     print('', 46, ''.center(width), '', 46, '')
                     print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                     width = 92
                     PATTERN = (input(" ".center(width)))

                     # SELECTING FROM VARIOUS PATTERNS......1
                     if PATTERN == '1':
                         width = 180
                         print('', 48, ''.rjust(width), '', 48, '')
                         print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                         print('', 50, ''.rjust(width), '', 50, '')

                         print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                         l = int(input("       ENTER LENGTH:"))
                         b = int(input("       ENTER BREADTH:"))
                         for i in range(1, l + 1):
                             for j in range(1, b + 1):
                                 if i == 1 or i == l or j == 1 or j == b:

                                     print('*', end=' ')
                                 else:
                                     print(' ', end=' ')
                             print()

                         print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                         # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                         n = int(input("       ENTER SIDE:"))
                         for i in range(1, n + 1):
                             for j in range(1, n + 1):
                                 if i == 1 or i == n or j == 1 or j == n:
                                     print('*', end=' ')
                                 else:
                                     print(' ', end=' ')
                             print()

                         print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                         row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                         col = row
                         for i in range(row):
                             for j in range(col):
                                 if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                         i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                         j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                     print('*', end=' ')  # end='' so that print statement should not change the line.

                                 else:
                                     print(' ', end=' ')  # to print the space.
                             print()  # to change the line after iteration of inner loop.

                         print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                         n = int(input("       ENTER HEIGHT:"))
                         for row in range(1, n + 1):
                             for col in range(1, 2 * n):
                                 if row == n or row + col == n + 1 or col - row == n - 1:
                                     print('*', end=' ')
                                 else:
                                     print(' ', end=' ')
                             print()



                     # SELECTING FROM VARIOUS PATTERNS......2
                     elif PATTERN == '2':
                         width = 180
                         print('', 48, ''.rjust(width), '', 48, '')
                         print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                         print('', 50, ''.rjust(width), '', 50, '')

                         # URSA MAJOR HEADING
                         msg = " 51"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "---- URSA MAJOR ----".center(width)
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "   51\n"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)

                         print()
                         width = 160  # URSA MAJOR PATTERN
                         print('*'.center(width))
                         width = 170
                         print('*'.center(width))
                         width = 175
                         print('*'.center(width))
                         print()
                         width = 185
                         print('*'.center(width))
                         width = 205
                         print('*'.center(width))
                         width = 188
                         print('*'.center(width))
                         width = 200
                         print('*'.center(width))  # /URSA MAJOR PATTERN
                         print()
                         print()

                         # URSA MINOR HEADING
                         width = 180
                         msg = " 52"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "---- URSA MINOR ----".center(width)
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "   52\n"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)

                         print()
                         width = 200  # URSA MINOR PATTERN
                         print('*'.center(width))
                         print()
                         width = 190
                         print('*'.center(width))
                         print()
                         width = 185
                         print('*'.center(width))
                         for i in range(1, 4):
                             print()
                         width = 188
                         print('*'.center(width))
                         width = 175
                         print('*'.center(width))
                         print()
                         print()
                         width = 193
                         print('*'.center(width))
                         width = 183
                         print('*'.center(width))  # /URSA MINOR PATTERN
                         print()
                         print()

                         # ORION HEADING
                         width = 180
                         msg = " 53"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "---- ORION ----".center(width)
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "   53\n"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)

                         print()
                         width = 200  # ORION PATTERN
                         print('*'.center(width))
                         print()
                         width = 170
                         print('*'.center(width))
                         print()
                         width = 210
                         print('*'.center(width))
                         for i in range(1, 7):
                             print()

                         width = 193
                         print('*'.center(width))
                         width = 188
                         print('*'.center(width))
                         width = 182
                         print('*'.center(width))
                         for i in range(1, 7):
                             print()
                         width = 210
                         print('*'.center(width))
                         width = 168
                         print('*'.center(width))   # /ORION PATTERN
                         print()
                         print()

                         # CASSIOPEIA HEADING
                         width = 180
                         msg = " 54"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "---- CASSIOPEIA ----".center(width)
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "   54\n"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)

                         print()
                         width = 210  # CASSIOPEIA PATTERN
                         print('*'.center(width))
                         print()
                         print()
                         width = 180
                         print('*'.center(width))
                         width = 207
                         print('*'.center(width))
                         width = 140
                         print('*'.center(width))
                         width = 173
                         print('*'.center(width))  # /CASSIOPEIA PATTERN
                         print()
                         print()

                         # ARIES HEADING
                         width = 180
                         msg = " 55"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "---- ARIES ----".center(width)
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)
                         msg = "   55\n"
                         for char in msg:
                             sys.stdout.write(char)
                             sys.stdout.flush()
                             time.sleep(0.01)

                         print()
                         width = 180  # ARIES PATTERN
                         print('*'.center(width))
                         print()
                         width = 200
                         print('*'.center(width))
                         width = 207
                         print('*'.center(width))
                         width = 205
                         print('*'.center(width))  # /ARIES PATTERN
                         print()


                #END OF CHOICE= 1 WHEN USER SAY 'NO'

                     '''END OF WHATTODO 1'''

                     # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                     width = 180
                     print()
                     print('', 55, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 55, '')
                     print()
                     width = 93
                     A_C2 = (input(" ".center(width)))
                     print()
                     if A_C2 == 'yes':
                         width = 180
                         print('', 56, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 56, '')
                         print()
                         print('', 57, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 57, '')
                         width = 95
                         print('', 58, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                             '                                '
                                                                             '                     ', 58, '')
                         width = 180
                         print('', 59, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 59, '')
                         width = 300
                         print('', 60,
                               'COMPOSITE NUMBERS(PRESS 4)                                         60'.center(width))
                         width = 180
                         print('', 61, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 61, '')
                         width = 93
                         number_seq = (input(" ".center(width)))

                         # SELECTING NUMBER SEQ. FROM ABOVE

                         # EVEN NUMBER.....
                         if number_seq == '1':
                             width = 180
                             print()
                             print('', 62, '---EVEN NUMBERS---'.center(width), '', 62, '')
                             print()
                             print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                   63, '')
                             width = 93
                             limit = int(input(" ".center(width)))
                             print()
                             if limit <= 50:
                                 for i in range(1, limit + 1):
                                     if i % 2 == 0:
                                         print(''.center(width), i, end=' ')
                                     print()
                             elif limit > 50:
                                 for i in range(1, limit + 1):
                                     if i % 2 == 0:
                                         print('', i, end=' ,')

                         # ODD NUMBER.....
                         elif number_seq == '2':
                             width = 180
                             print()
                             print('', 62, '---ODD NUMBERS---'.center(width), '', 62, '')
                             print()
                             print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                   63, '')
                             width = 93
                             limit = int(input(" ".center(width)))
                             print()
                             if limit <= 50:
                                 for i in range(1, limit + 1):
                                     if i % 2 != 0:
                                         print(''.center(width), i, end=' ')
                                     print()
                             elif limit > 50:
                                 for i in range(1, limit + 1):
                                     if i % 2 != 0:
                                         print('', i, end=' ,')


                         # PRIME NUMBERS.....
                         elif number_seq == '3':
                             width = 180
                             print()
                             print('', 62, '---PRIME NUMBERS---'.center(width), '', 62, '')
                             print()
                             print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                   63, '')
                             width = 93
                             limit = int(input(" ".center(width)))
                             print()
                             if limit <= 50:
                                 print(''.center(width), '2')
                                 for i in range(1, limit + 1):
                                     if i != 1 and i % 2 != 0:
                                         print(''.center(width), i, end=' ')
                                     print()
                             elif limit > 50:
                                 print('2 ,', end='')
                                 for i in range(1, limit + 1):
                                     if i != 1 and i % 2 != 0:
                                         print('', i, end=' ,')


                         # COMPOSITE NUMBERS.....
                         elif number_seq == '4':
                             width = 180
                             print()
                             print('', 62, '---COMPOSITE NUMBERS---'.center(width), '', 62, '')
                             print()
                             print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                   '', 63, '')
                             width = 93
                             limit = int(input(" ".center(width)))
                             print()
                             if limit <= 50:
                                 for i in range(4, limit + 1):
                                     if i % 2 == 0:
                                         print(''.center(width), i, end=' ')
                                     print()
                             elif limit > 50:
                                 for i in range(4, limit + 1):
                                     if i % 2 == 0:
                                         print('', i, end=' ,')


                         # FIBONACCHI NUMBERS.....
                         elif number_seq == '5':
                             width = 180
                             print()
                             print('', 62, '---FIBONACCHI NUMBERS---'.center(width), '', 62, '')
                             print()
                             print('', 63,
                                   'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                   '', 63, '')
                             width = 93
                             limit = int(input(" ".center(width)))
                             print()
                             if limit <= 25:
                                 a, b = 1, 1
                                 print(''.center(width), a)
                                 print()
                                 print(''.center(width), b)
                                 print()
                                 for i in range(limit - 2):
                                     c = a + b
                                     b = a
                                     a = c
                                     print(''.center(width), c, end='\n')
                                     print()
                             elif limit > 25:
                                 a, b = 1, 1
                                 print(a, ',', end='')
                                 print('', b, ',', end='')
                                 for i in range(limit - 2):
                                     c = a + b
                                     b = a
                                     a = c
                                     print('', c, end=' ,')

                             '''END OF WHATTODO=2'''

                             # END OF CHOICE= 2
                             width = 180
                             print()
                             msg = " 64"
                             for char in msg:
                                 sys.stdout.write(char)
                                 sys.stdout.flush()
                                 time.sleep(0.01)
                             msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                             for char in msg:
                                 sys.stdout.write(char)
                                 sys.stdout.flush()
                                 time.sleep(0.01)
                             msg = "   64\n"
                             for char in msg:
                                 sys.stdout.write(char)
                                 sys.stdout.flush()
                                 time.sleep(0.01)
                             for i in range(65, 71):
                                 print('', i, ''.rjust(width), '', i, '')

                     elif A_C2 == 'no':
                         width = 180
                         print()
                         print('', 55, 'OK BYE'.center(width), '', 55, '')
                         print('', 56, 'ENJOY YOUR DAY :)'.center(width), '', 56, '')
                         for i in range(57, 61):
                             print('', i, ''.rjust(width), '', i, '')

                             '''WHATTODO FINALLY FINISHED'''




            # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
            elif CHOICE=='2':
                width = 180
                print('', 30, ''.rjust(width), '', 30, '')
                print('', 31, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 31, '')
                print('', 31, 'WELCOME TO PATTERNS'.center(width), '', 31, '')
                print('', 32, ''.rjust(width), '', 32, '')
                print('', 33, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 33, '')
                print('', 34, ''.rjust(width), '', 34, '')
                print('', 35, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 35, '')
                print('', 36, ''.center(width), '', 36, '')
                print('', 37, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 37, '')
                width = 92
                PATTERN = (input(" ".center(width)))

                #SELECTING FROM VARIOUS PATTERNS......1
                if PATTERN=='1':
                    width=180
                    print('', 38, ''.rjust(width), '', 38, '')
                    print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                    print('', 40, ''.rjust(width), '', 40, '')

                    print('', 41, '* RECTANGLE'.ljust(width), '', 41, '')                       #RECTANGLE IS MADE HERE
                    l = int(input("       ENTER LENGTH:"))
                    b = int(input("       ENTER BREADTH:"))
                    for i in range(1, l + 1):
                        for j in range(1, b + 1):
                            if i == 1 or i == l or j == 1 or j == b:

                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()



                    print('', 42, '* SQUARE'.ljust(width), '', 42, '')                            #SQUARE IS MADE HERE
                    #NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                    n = int(input("       ENTER SIDE:"))
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i == 1 or i == n or j == 1 or j == n:
                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()


                    print('', 43, '* CIRCLE'.ljust(width), '', 43, '')                             #CIRCLE IS MADE HERE
                    row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                    col = row
                    for i in range(row):
                        for j in range(col):
                            if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                    i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                    j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                print('*', end=' ')  # end='' so that print statement should not change the line.

                            else:
                                print(' ', end=' ')  # to print the space.
                        print()  # to change the line after iteration of inner loop.

                    print('', 44, '* TRIANGLE'.ljust(width), '', 44, '')                         #TRIANGLE IS MADE HERE
                    n = int(input("       ENTER HEIGHT:"))
                    for row in range(1, n + 1):
                        for col in range(1, 2 * n):
                            if row == n or row + col == n + 1 or col - row == n - 1:
                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()

                    '''END OF WHATTODO 1'''

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45, '')
                    print()
                    width = 93
                    AC = (input(" ".center(width)))
                    print()
                    if AC == 'yes':
                        width = 180
                        print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                        print()
                        print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                        width = 95
                        print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 48, '')
                        width = 180
                        print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                        width = 300
                        print('', 50,
                              'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(width))
                        width = 180
                        print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                            '''END OF WHATTODO=2'''

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(55, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif AC == 'no':
                        width = 180
                        print()
                        print('', 46, 'OK BYE'.center(width), '', 46, '')
                        print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                        for i in range(48, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''


                #SELECTING FROM VARIOUS PATTERNS......2
                elif PATTERN == '2':
                    width = 180
                    print('', 38, ''.rjust(width), '', 38, '')
                    print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                    print('', 40, ''.rjust(width), '', 40, '')



                    # URSA MAJOR HEADING
                    msg = " 41"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- URSA MAJOR ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   41\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 160                                         #URSA MAJOR PATTERN
                    print('*'.center(width))
                    width = 170
                    print('*'.center(width))
                    width = 175
                    print('*'.center(width))
                    print()
                    width = 185
                    print('*'.center(width))
                    width = 205
                    print('*'.center(width))
                    width = 188
                    print('*'.center(width))
                    width = 200
                    print('*'.center(width))                              # /URSA MAJOR PATTERN
                    print()
                    print()


                    # URSA MINOR HEADING
                    width=180
                    msg = " 42"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- URSA MINOR ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   42\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 200                                   #URSA MINOR PATTERN
                    print('*'.center(width))
                    print()
                    width = 190
                    print('*'.center(width))
                    print()
                    width = 185
                    print('*'.center(width))
                    for i in range(1, 4):
                        print()
                    width = 188
                    print('*'.center(width))
                    width = 175
                    print('*'.center(width))
                    print()
                    print()
                    width = 193
                    print('*'.center(width))
                    width = 183
                    print('*'.center(width))                      # /URSA MINOR PATTERN
                    print()
                    print()


                    # ORION HEADING
                    width=180
                    msg = " 43"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- ORION ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   43\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 200                                    # ORION PATTERN
                    print('*'.center(width))
                    print()
                    width = 170
                    print('*'.center(width))
                    print()
                    width = 210
                    print('*'.center(width))
                    for i in range(1, 7):
                        print()

                    width = 193
                    print('*'.center(width))
                    width = 188
                    print('*'.center(width))
                    width = 182
                    print('*'.center(width))
                    for i in range(1, 7):
                        print()
                    width = 210
                    print('*'.center(width))
                    width = 168
                    print('*'.center(width))                        # /ORION PATTERN
                    print()
                    print()


                    # CASSIOPEIA HEADING
                    width=180
                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- CASSIOPEIA ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 210                                     # CASSIOPEIA PATTERN
                    print('*'.center(width))
                    print()
                    print()
                    width = 180
                    print('*'.center(width))
                    width = 207
                    print('*'.center(width))
                    width = 140
                    print('*'.center(width))
                    width = 173
                    print('*'.center(width))                        # /CASSIOPEIA PATTERN
                    print()
                    print()

                    # ARIES HEADING
                    width=180
                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- ARIES ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 180                                       # ARIES PATTERN
                    print('*'.center(width))
                    print()
                    width = 200
                    print('*'.center(width))
                    width = 207
                    print('*'.center(width))
                    width = 205
                    print('*'.center(width))                          # /ARIES PATTERN
                    print()


                    '''END OF WHATTODO 1'''

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45, '')
                    print()
                    width = 93
                    AC = (input(" ".center(width)))
                    print()
                    if AC == 'yes':
                        width = 180
                        print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                        print()
                        print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                        width = 95
                        print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 48, '')
                        width = 180
                        print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                        width = 300
                        print('', 50,
                              'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(width))
                        width = 180
                        print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')



                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(55, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif AC == 'no':
                        width = 180
                        print()
                        print('', 46, 'OK BYE'.center(width), '', 46, '')
                        print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                        for i in range(48, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''



        #SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 2)
        elif WHATTODO == '2':
            width = 180
            print('', 26, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 26, '')
            print()
            print('', 27, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 27, '')
            width=95
            print('', 28, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                '                                '
                                                                '                     ', 28, '')
            width=180
            print('', 29, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 29, '')
            width=300
            print('', 30, 'COMPOSITE NUMBERS(PRESS 4)                                         30'.center(width))
            width=180
            print('', 31, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 31, '')
            width = 93
            number_seq = (input(" ".center(width)))

            #SELECTING NUMBER SEQ. FROM ABOVE

            # EVEN NUMBER.....
            if number_seq=='1':
                width = 180
                print()
                print('', 32, '---EVEN NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(1, limit + 1):
                        if i % 2 == 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(1, limit + 1):
                        if i % 2 == 0:
                            print('', i, end=' ,')

            # ODD NUMBER.....
            elif number_seq == '2':
                width = 180
                print()
                print('', 32, '---ODD NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(1, limit + 1):
                        if i % 2 != 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(1, limit + 1):
                        if i % 2 != 0:
                            print('', i, end=' ,')


            # PRIME NUMBERS.....
            elif number_seq == '3':
                width = 180
                print()
                print('', 32, '---PRIME NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    print(''.center(width), '2')
                    for i in range(1, limit + 1):
                        if i != 1 and i % 2 != 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    print('2 ,', end='')
                    for i in range(1, limit + 1):
                        if i != 1 and i % 2 != 0:
                            print('', i, end=' ,')


            # COMPOSITE NUMBERS.....
            elif number_seq == '4':
                width = 180
                print()
                print('', 32, '---COMPOSITE NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(4, limit + 1):
                        if i % 2 == 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(4, limit + 1):
                        if i % 2 == 0:
                            print('', i, end=' ,')


            # FIBONACCHI NUMBERS.....
            elif number_seq == '5':
                width = 180
                print()
                print('', 32, '---FIBONACCHI NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 25:
                    a, b = 1, 1
                    print(''.center(width), a)
                    print()
                    print(''.center(width), b)
                    print()
                    for i in range(limit - 2):
                        c = a + b
                        b = a
                        a = c
                        print(''.center(width), c, end='\n')
                        print()
                elif limit > 25:
                    a, b = 1, 1
                    print(a, ',', end='')
                    print('', b, ',', end='')
                    for i in range(limit - 2):
                        c = a + b
                        b = a
                        a = c
                        print('', c, end=' ,')              #END OF WHAT TO DO 2

            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER
            width = 180
            print()
            print('', 34, ' DO YOU WANT TO PLAY WITH NUMBERS TOO?(yes or no)'.center(width), '', 34, '')
            print()
            width = 93
            A_C = (input(" ".center(width)))
            print()
            if A_C == 'yes':
                width = 180
                print('', 35, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 35, '')

                # 1st choice

                msg = " 36"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   36\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                # 2nd choice

                msg = " 37"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   37\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                print('', 38, ''.rjust(width), '', 38, '')

                width = 92
                CHOICE = (input(" ".center(width)))

                # SELECTING FROM VARIOUS CHOICES GIVEN
                if CHOICE == '1':

                    # ALLEN ASSISTANT

                    width = 180
                    print('', 39, ''.rjust(width), '', 39, '')
                    print('', 40, 'WELCOME TO MAGICA'.center(width), '', 40, '')
                    print('', 41, ''.rjust(width), '', 41, '')
                    print('', 42, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 42, '')
                    print('', 43, ''.rjust(width), '', 43, '')

                    width = 173
                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # ALLEN USER TALK:-
                    print()
                    USER = (input("      YOU-"))  # ALLEN USER TALK 1
                    print()
                    # /ALLEN USER TALK:-

                    # WHEN USER SAID YES
                    if USER == 'yes':  # when user said yes to allen

                        msg = " 46"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   46\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN 3 DOTS

                        msg = " 47"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print(' ALLEN-', end='')
                        msg = "......".ljust(width)  # A 4TH LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   47\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)  #

                        msg = " 48"  # ALLEN CONTINUES TO TALK
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   48\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                        msg = " 49"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                            width)  # A 6TH LINE AND STEP 1
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   49\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 50"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(width)  # A 7TH LINE AND STEP 2
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   50\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 51"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                            width)  # A 8TH LINE AND STEP 3
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   51\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 52"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   52\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 53"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                            width)  # A 10TH LINE AND STEP 5
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   53\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                            width)  # A 11TH LINE AND PART OF STEP 5
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                            width)  # A 12TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 56"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                            width)  # A 13TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        msg = "   56\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN USER TALK:-
                        print()
                        USER_ANS = int(input("    YOUR ANS-"))
                        USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                        DIFF = USER_ANS - USER_ANS2
                        AGE = DIFF % 100
                        CHOOSEN_NO = DIFF // 100
                        print()
                        # /ALLEN USER TALK:-

                        msg = " 57"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print(' ALLEN-', end='')
                        msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                            width)  # A 14TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   57\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print()
                        print('    ALLEN- ', end='')
                        print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                        print(AGE, "YEARS")

                        print('    ALLEN- ', end='')
                        print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                              end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                        print(CHOOSEN_NO)
                        print()

                        # END OF CHOICE= 1 WHEN USER SAY 'YES'
                        width = 180
                        print()
                        msg = " 58"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   58\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(59, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    # WHEN USER SAID NO
                    elif USER == 'no':  # when user said no to allen

                        msg = " 46"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   46\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 47"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   47\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # OFFERING 2ND CHOICE TO USER.................................
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 49, '')
                        print('', 50, 'WELCOME TO PATTERNS'.center(width), '', 50, '')
                        print('', 51, ''.rjust(width), '', 51, '')
                        print('', 52, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 52, '')
                        print('', 53, ''.rjust(width), '', 53, '')
                        print('', 54, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 54, '')
                        print('', 55, ''.center(width), '', 55, '')
                        print('', 56, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 56, '')
                        width = 92
                        PATTERN = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS PATTERNS......1
                        if PATTERN == '1':
                            width = 180
                            print('', 57, ''.rjust(width), '', 57, '')
                            print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                            print('', 59, ''.rjust(width), '', 59, '')

                            print('', 60, '* RECTANGLE'.ljust(width), '', 60, '')  # RECTANGLE IS MADE HERE
                            l = int(input("       ENTER LENGTH:"))
                            b = int(input("       ENTER BREADTH:"))
                            for i in range(1, l + 1):
                                for j in range(1, b + 1):
                                    if i == 1 or i == l or j == 1 or j == b:

                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 61, '* SQUARE'.ljust(width), '', 61, '')  # SQUARE IS MADE HERE
                            # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                            n = int(input("       ENTER SIDE:"))
                            for i in range(1, n + 1):
                                for j in range(1, n + 1):
                                    if i == 1 or i == n or j == 1 or j == n:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 62, '* CIRCLE'.ljust(width), '', 62, '')  # CIRCLE IS MADE HERE
                            row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                            col = row
                            for i in range(row):
                                for j in range(col):
                                    if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                            i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                            j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                        print('*',
                                              end=' ')  # end='' so that print statement should not change the line.

                                    else:
                                        print(' ', end=' ')  # to print the space.
                                print()  # to change the line after iteration of inner loop.

                            print('', 63, '* TRIANGLE'.ljust(width), '', 63, '')  # TRIANGLE IS MADE HERE
                            n = int(input("       ENTER HEIGHT:"))
                            for row in range(1, n + 1):
                                for col in range(1, 2 * n):
                                    if row == n or row + col == n + 1 or col - row == n - 1:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()



                        # SELECTING FROM VARIOUS PATTERNS......2
                        elif PATTERN == '2':
                            width = 180
                            print('', 57, ''.rjust(width), '', 57, '')
                            print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                            print('', 59, ''.rjust(width), '', 59, '')

                            # URSA MAJOR HEADING
                            msg = " 60"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MAJOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   60\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 160  # URSA MAJOR PATTERN
                            print('*'.center(width))
                            width = 170
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 200
                            print('*'.center(width))  # /URSA MAJOR PATTERN
                            print()
                            print()

                            # URSA MINOR HEADING
                            width = 180
                            msg = " 61"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MINOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   61\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # URSA MINOR PATTERN
                            print('*'.center(width))
                            print()
                            width = 190
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            for i in range(1, 4):
                                print()
                            width = 188
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            print()
                            width = 193
                            print('*'.center(width))
                            width = 183
                            print('*'.center(width))  # /URSA MINOR PATTERN
                            print()
                            print()

                            # ORION HEADING
                            width = 180
                            msg = " 62"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ORION ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   62\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # ORION PATTERN
                            print('*'.center(width))
                            print()
                            width = 170
                            print('*'.center(width))
                            print()
                            width = 210
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()

                            width = 193
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 182
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()
                            width = 210
                            print('*'.center(width))
                            width = 168
                            print('*'.center(width))  # /ORION PATTERN
                            print()
                            print()

                            # CASSIOPEIA HEADING
                            width = 180
                            msg = " 63"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- CASSIOPEIA ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   63\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 210  # CASSIOPEIA PATTERN
                            print('*'.center(width))
                            print()
                            print()
                            width = 180
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 140
                            print('*'.center(width))
                            width = 173
                            print('*'.center(width))  # /CASSIOPEIA PATTERN
                            print()
                            print()

                            # ARIES HEADING
                            width = 180
                            msg = " 64"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ARIES ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   64\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 180  # ARIES PATTERN
                            print('*'.center(width))
                            print()
                            width = 200
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))  # /ARIES PATTERN
                            print()

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 64"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   64\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(65, 71):
                            print('', i, ''.rjust(width), '', i, '')

                    # END OF CHOICE= 1 WHEN USER SAY 'NO'





                # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                elif CHOICE == '2':
                    width = 180
                    print('', 39, ''.rjust(width), '', 39, '')
                    print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                    print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                    print('', 42, ''.rjust(width), '', 42, '')
                    print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                    print('', 44, ''.rjust(width), '', 44, '')
                    print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                    print('', 46, ''.center(width), '', 46, '')
                    print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                    width = 92
                    PATTERN = (input(" ".center(width)))

                    # SELECTING FROM VARIOUS PATTERNS......1
                    if PATTERN == '1':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                        l = int(input("       ENTER LENGTH:"))
                        b = int(input("       ENTER BREADTH:"))
                        for i in range(1, l + 1):
                            for j in range(1, b + 1):
                                if i == 1 or i == l or j == 1 or j == b:

                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                        # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                        n = int(input("       ENTER SIDE:"))
                        for i in range(1, n + 1):
                            for j in range(1, n + 1):
                                if i == 1 or i == n or j == 1 or j == n:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                        row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                        col = row
                        for i in range(row):
                            for j in range(col):
                                if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                        i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                        j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                    print('*', end=' ')  # end='' so that print statement should not change the line.

                                else:
                                    print(' ', end=' ')  # to print the space.
                            print()  # to change the line after iteration of inner loop.

                        print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                        n = int(input("       ENTER HEIGHT:"))
                        for row in range(1, n + 1):
                            for col in range(1, 2 * n):
                                if row == n or row + col == n + 1 or col - row == n - 1:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()



                    # SELECTING FROM VARIOUS PATTERNS......2
                    elif PATTERN == '2':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        # URSA MAJOR HEADING
                        msg = " 51"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MAJOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   51\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 160  # URSA MAJOR PATTERN
                        print('*'.center(width))
                        width = 170
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 200
                        print('*'.center(width))  # /URSA MAJOR PATTERN
                        print()
                        print()

                        # URSA MINOR HEADING
                        width = 180
                        msg = " 52"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MINOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   52\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # URSA MINOR PATTERN
                        print('*'.center(width))
                        print()
                        width = 190
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        for i in range(1, 4):
                            print()
                        width = 188
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        print()
                        width = 193
                        print('*'.center(width))
                        width = 183
                        print('*'.center(width))  # /URSA MINOR PATTERN
                        print()
                        print()

                        # ORION HEADING
                        width = 180
                        msg = " 53"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ORION ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   53\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # ORION PATTERN
                        print('*'.center(width))
                        print()
                        width = 170
                        print('*'.center(width))
                        print()
                        width = 210
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()

                        width = 193
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 182
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()
                        width = 210
                        print('*'.center(width))
                        width = 168
                        print('*'.center(width))  # /ORION PATTERN
                        print()
                        print()

                        # CASSIOPEIA HEADING
                        width = 180
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- CASSIOPEIA ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 210  # CASSIOPEIA PATTERN
                        print('*'.center(width))
                        print()
                        print()
                        width = 180
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 140
                        print('*'.center(width))
                        width = 173
                        print('*'.center(width))  # /CASSIOPEIA PATTERN
                        print()
                        print()

                        # ARIES HEADING
                        width = 180
                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ARIES ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 180  # ARIES PATTERN
                        print('*'.center(width))
                        print()
                        width = 200
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))  # /ARIES PATTERN
                        print()

                # END OF CHOICE= 2
                width = 180
                print()
                msg = " 55"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   55\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                for i in range(56, 61):
                    print('', i, ''.rjust(width), '', i, '')

                # MORE  ABOVE CODING  OF PLAY WITH NUMBERS..........................................................


            elif A_C == 'no':
                width = 180
                print()
                print('', 35, 'OK BYE'.center(width), '', 35, '')
                print('', 36, 'ENJOY YOUR DAY :)'.center(width), '', 36, '')
                for i in range(37, 51):
                    print('', i, ''.rjust(width), '', i, '')

                    '''WHATTODO FINALLY FINISHED'''



   # FINISHED WHEN THE ANSWER OF 2ND QUESTION IS RIGHT IN THE FIRST TRY...................





    #IF THE ANSWER IS WRONG:GIVING ANOTHER CHANCE'''
    else:
        print('', 18, ''.rjust(width), '', 18, '')
        print('', 19, '|OHH SORRY! YOU ARE WRONG|'.center(width), '', 19, '')
        print('', 20, ' DO YOU WANT TO GIVE IT ANOTHER TRY (yes or no)'.center(width), '', 20, '')
        width = 92
        C = (input(" ".center(width)))

        '''IF THE USER AGREES TO TRY AGAIN'''
        if C == 'yes':
            width = 180
            print()
            print('', 21, 'TYPE YOUR ANSWER AGAIN:-'.center(width), '', 21, '')

            width = 92
            D = (input(" ".center(width)))
            width = 180
            '''IF  2ND  ANSWER IS CORRECT'''
            if D == '70':
                print('', "*", ''.rjust(width), '', " *", '')
                print('', "*", 'YOU GOT IT RIGHT...FINALLY!'.center(width), '', " *", '')
                print('', "*", '|YOU ARE SUCCESSFULLY LOGGED IN|'.center(width), '', " *", '')
                print('', "*", ''.rjust(width), '', " *", '')

                # MAIN TOPIC STARTS FROM HERE I.E. WHAT TO DO WITH NUMBERS

                print()
                print('', 22, 'NOW SELECT WHAT DO YOU WANT TO DO WITH NUMBERS'.center(width), '', 22, '')
                print('', 23, 'PLAY WITH NUMBERS(PRESS 1)'.ljust(width), '', 23, '')
                print('', 24, 'OR'.center(width), '', 24, '')
                print('', 25, 'FIND OUT VARIOUS NUMBER SEQUENCE(PRESS 2)'.rjust(width), '', 25, '')
                width = 93
                WHATTODO = (input(" ".center(width)))

                # PLAY WITH NUMBERS LOOP START FROM HERE WITH 2 CHOICES

                # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 1)
                if WHATTODO == '1':
                    width = 180
                    print('', 26, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 26, '')

                    # 1st choice

                    msg = " 27"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   27\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # 2nd choice

                    msg = " 28"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   28\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print('', 29, ''.rjust(width), '', 29, '')

                    width = 92
                    CHOICE = (input(" ".center(width)))

                    # SELECTING FROM VARIOUS CHOICES GIVEN
                    if CHOICE == '1':

                        # ALLEN ASSISTANT

                        width = 180
                        print('', 30, ''.rjust(width), '', 30, '')
                        print('', 31, 'WELCOME TO MAGICA'.center(width), '', 31, '')
                        print('', 32, ''.rjust(width), '', 32, '')
                        print('', 33, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 33, '')
                        print('', 34, ''.rjust(width), '', 34, '')

                        width = 173
                        msg = " 35"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   35\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 36"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   36\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN USER TALK:-
                        print()
                        USER = (input("      YOU-"))  # ALLEN USER TALK 1
                        print()
                        # /ALLEN USER TALK:-

                        # WHEN USER SAID YES
                        if USER == 'yes':  # when user said yes to allen

                            msg = " 37"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   37\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN 3 DOTS

                            msg = " 38"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print(' ALLEN-', end='')
                            msg = "......".ljust(width)  # A 4TH LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   38\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)  #

                            msg = " 39"  # ALLEN CONTINUES TO TALK
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   39\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                            msg = " 40"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                                width)  # A 6TH LINE AND STEP 1
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   40\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 41"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(
                                width)  # A 7TH LINE AND STEP 2
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   41\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 42"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                                width)  # A 8TH LINE AND STEP 3
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   42\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 43"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   43\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                                width)  # A 10TH LINE AND STEP 5
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                                width)  # A 11TH LINE AND PART OF STEP 5
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 46"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                                width)  # A 12TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            msg = "   46\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 47"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                                width)  # A 13TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            msg = "   47\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN USER TALK:-
                            print()
                            USER_ANS = int(input("    YOUR ANS-"))
                            USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                            DIFF = USER_ANS - USER_ANS2
                            AGE = DIFF % 100
                            CHOOSEN_NO = DIFF // 100
                            print()
                            # /ALLEN USER TALK:-

                            msg = " 48"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print(' ALLEN-', end='')
                            msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                                width)  # A 14TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   48\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)

                            print()
                            print('    ALLEN- ', end='')
                            print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                            print(AGE, "YEARS")

                            print('    ALLEN- ', end='')
                            print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                                  end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                            print(CHOOSEN_NO)
                            print()

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 49, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 49,
                                  '')
                            print()
                            width = 93
                            A_C2 = (input(" ".center(width)))
                            print()
                            if A_C2 == 'yes':
                                width = 180
                                print('', 50, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 50, '')
                                print()
                                print('', 51, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 51, '')
                                width = 95
                                print('', 52, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 52, '')
                                width = 180
                                print('', 53, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 53, '')
                                width = 300
                                print('', 54,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         54'.center(
                                          width))
                                width = 180
                                print('', 55, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 55, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 56, '---EVEN NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 56, '---ODD NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 56, '---PRIME NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 56, '---COMPOSITE NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 56, '---FIBONACCHI NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                '''END OF WHATTODO=2'''

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 58"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   58\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(59, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif A_C2 == 'no':
                                width = 180
                                print()
                                print('', 49, 'OK BYE'.center(width), '', 49, '')
                                print('', 50, 'ENJOY YOUR DAY :)'.center(width), '', 50, '')
                                for i in range(51, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''MAGIC YES FINALLY FINISHED'''

                        # WHEN USER SAID NO
                        elif USER == 'no':  # when user said no to allen

                            msg = " 37"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   37\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 38"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   38\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # OFFERING 2ND CHOICE TO USER.................................
                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                            print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                            print('', 42, ''.rjust(width), '', 42, '')
                            print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                            print('', 44, ''.rjust(width), '', 44, '')
                            print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                            print('', 46, ''.center(width), '', 46, '')
                            print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                            width = 92
                            PATTERN = (input(" ".center(width)))

                            # SELECTING FROM VARIOUS PATTERNS......1
                            if PATTERN == '1':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                                l = int(input("       ENTER LENGTH:"))
                                b = int(input("       ENTER BREADTH:"))
                                for i in range(1, l + 1):
                                    for j in range(1, b + 1):
                                        if i == 1 or i == l or j == 1 or j == b:

                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                                # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                n = int(input("       ENTER SIDE:"))
                                for i in range(1, n + 1):
                                    for j in range(1, n + 1):
                                        if i == 1 or i == n or j == 1 or j == n:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                                row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                col = row
                                for i in range(row):
                                    for j in range(col):
                                        if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                            print('*',
                                                  end=' ')  # end='' so that print statement should not change the line.

                                        else:
                                            print(' ', end=' ')  # to print the space.
                                    print()  # to change the line after iteration of inner loop.

                                print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                                n = int(input("       ENTER HEIGHT:"))
                                for row in range(1, n + 1):
                                    for col in range(1, 2 * n):
                                        if row == n or row + col == n + 1 or col - row == n - 1:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()



                            # SELECTING FROM VARIOUS PATTERNS......2
                            elif PATTERN == '2':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                # URSA MAJOR HEADING
                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MAJOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 160  # URSA MAJOR PATTERN
                                print('*'.center(width))
                                width = 170
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 200
                                print('*'.center(width))  # /URSA MAJOR PATTERN
                                print()
                                print()

                                # URSA MINOR HEADING
                                width = 180
                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MINOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # URSA MINOR PATTERN
                                print('*'.center(width))
                                print()
                                width = 190
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                for i in range(1, 4):
                                    print()
                                width = 188
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                print()
                                width = 193
                                print('*'.center(width))
                                width = 183
                                print('*'.center(width))  # /URSA MINOR PATTERN
                                print()
                                print()

                                # ORION HEADING
                                width = 180
                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ORION ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # ORION PATTERN
                                print('*'.center(width))
                                print()
                                width = 170
                                print('*'.center(width))
                                print()
                                width = 210
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()

                                width = 193
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 182
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()
                                width = 210
                                print('*'.center(width))
                                width = 168
                                print('*'.center(width))  # /ORION PATTERN
                                print()
                                print()

                                # CASSIOPEIA HEADING
                                width = 180
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- CASSIOPEIA ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 210  # CASSIOPEIA PATTERN
                                print('*'.center(width))
                                print()
                                print()
                                width = 180
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 140
                                print('*'.center(width))
                                width = 173
                                print('*'.center(width))  # /CASSIOPEIA PATTERN
                                print()
                                print()

                                # ARIES HEADING
                                width = 180
                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ARIES ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 180  # ARIES PATTERN
                                print('*'.center(width))
                                print()
                                width = 200
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))  # /ARIES PATTERN
                                print()

                            # END OF CHOICE= 1 WHEN USER SAY 'NO'

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 55, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 55,
                                  '')
                            print()
                            width = 93
                            A_C2 = (input(" ".center(width)))
                            print()
                            if A_C2 == 'yes':
                                width = 180
                                print('', 56, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 56, '')
                                print()
                                print('', 57, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 57, '')
                                width = 95
                                print('', 58, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 58, '')
                                width = 180
                                print('', 59, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 59, '')
                                width = 300
                                print('', 60,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         60'.center(
                                          width))
                                width = 180
                                print('', 61, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 61, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 62, '---EVEN NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 62, '---ODD NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 62, '---PRIME NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 62, '---COMPOSITE NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 62, '---FIBONACCHI NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                            # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 64"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   64\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(65, 71):
                                    print('', i, ''.rjust(width), '', i, '')



                            elif A_C2 == 'no':
                                width = 180
                                print()
                                print('', 55, 'OK BYE'.center(width), '', 55, '')
                                print('', 56, 'ENJOY YOUR DAY :)'.center(width), '', 56, '')
                                for i in range(57, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''




                    # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                    elif CHOICE == '2':
                        width = 180
                        print('', 30, ''.rjust(width), '', 30, '')
                        print('', 31, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 31, '')
                        print('', 31, 'WELCOME TO PATTERNS'.center(width), '', 31, '')
                        print('', 32, ''.rjust(width), '', 32, '')
                        print('', 33, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 33, '')
                        print('', 34, ''.rjust(width), '', 34, '')
                        print('', 35, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 35, '')
                        print('', 36, ''.center(width), '', 36, '')
                        print('', 37, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 37, '')
                        width = 92
                        PATTERN = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS PATTERNS......1
                        if PATTERN == '1':
                            width = 180
                            print('', 38, ''.rjust(width), '', 38, '')
                            print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                            print('', 40, ''.rjust(width), '', 40, '')

                            print('', 41, '* RECTANGLE'.ljust(width), '', 41, '')  # RECTANGLE IS MADE HERE
                            l = int(input("       ENTER LENGTH:"))
                            b = int(input("       ENTER BREADTH:"))
                            for i in range(1, l + 1):
                                for j in range(1, b + 1):
                                    if i == 1 or i == l or j == 1 or j == b:

                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 42, '* SQUARE'.ljust(width), '', 42, '')  # SQUARE IS MADE HERE
                            # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                            n = int(input("       ENTER SIDE:"))
                            for i in range(1, n + 1):
                                for j in range(1, n + 1):
                                    if i == 1 or i == n or j == 1 or j == n:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 43, '* CIRCLE'.ljust(width), '', 43, '')  # CIRCLE IS MADE HERE
                            row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                            col = row
                            for i in range(row):
                                for j in range(col):
                                    if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                            i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                            j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                        print('*',
                                              end=' ')  # end='' so that print statement should not change the line.

                                    else:
                                        print(' ', end=' ')  # to print the space.
                                print()  # to change the line after iteration of inner loop.

                            print('', 44, '* TRIANGLE'.ljust(width), '', 44, '')  # TRIANGLE IS MADE HERE
                            n = int(input("       ENTER HEIGHT:"))
                            for row in range(1, n + 1):
                                for col in range(1, 2 * n):
                                    if row == n or row + col == n + 1 or col - row == n - 1:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45,
                                  '')
                            print()
                            width = 93
                            AC = (input(" ".center(width)))
                            print()
                            if AC == 'yes':
                                width = 180
                                print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                                print()
                                print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                                width = 95
                                print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 48, '')
                                width = 180
                                print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                                width = 300
                                print('', 50,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(
                                          width))
                                width = 180
                                print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                    '''END OF WHATTODO=2'''

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(55, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif AC == 'no':
                                width = 180
                                print()
                                print('', 46, 'OK BYE'.center(width), '', 46, '')
                                print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                                for i in range(48, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''


                        # SELECTING FROM VARIOUS PATTERNS......2
                        elif PATTERN == '2':
                            width = 180
                            print('', 38, ''.rjust(width), '', 38, '')
                            print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                            print('', 40, ''.rjust(width), '', 40, '')

                            # URSA MAJOR HEADING
                            msg = " 41"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MAJOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   41\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 160  # URSA MAJOR PATTERN
                            print('*'.center(width))
                            width = 170
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 200
                            print('*'.center(width))  # /URSA MAJOR PATTERN
                            print()
                            print()

                            # URSA MINOR HEADING
                            width = 180
                            msg = " 42"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MINOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   42\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # URSA MINOR PATTERN
                            print('*'.center(width))
                            print()
                            width = 190
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            for i in range(1, 4):
                                print()
                            width = 188
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            print()
                            width = 193
                            print('*'.center(width))
                            width = 183
                            print('*'.center(width))  # /URSA MINOR PATTERN
                            print()
                            print()

                            # ORION HEADING
                            width = 180
                            msg = " 43"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ORION ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   43\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # ORION PATTERN
                            print('*'.center(width))
                            print()
                            width = 170
                            print('*'.center(width))
                            print()
                            width = 210
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()

                            width = 193
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 182
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()
                            width = 210
                            print('*'.center(width))
                            width = 168
                            print('*'.center(width))  # /ORION PATTERN
                            print()
                            print()

                            # CASSIOPEIA HEADING
                            width = 180
                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- CASSIOPEIA ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 210  # CASSIOPEIA PATTERN
                            print('*'.center(width))
                            print()
                            print()
                            width = 180
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 140
                            print('*'.center(width))
                            width = 173
                            print('*'.center(width))  # /CASSIOPEIA PATTERN
                            print()
                            print()

                            # ARIES HEADING
                            width = 180
                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ARIES ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 180  # ARIES PATTERN
                            print('*'.center(width))
                            print()
                            width = 200
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))  # /ARIES PATTERN
                            print()

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45,
                                  '')
                            print()
                            width = 93
                            AC = (input(" ".center(width)))
                            print()
                            if AC == 'yes':
                                width = 180
                                print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                                print()
                                print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                                width = 95
                                print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 48, '')
                                width = 180
                                print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                                width = 300
                                print('', 50,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(
                                          width))
                                width = 180
                                print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(55, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif AC == 'no':
                                width = 180
                                print()
                                print('', 46, 'OK BYE'.center(width), '', 46, '')
                                print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                                for i in range(48, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''



                # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 2)
                elif WHATTODO == '2':
                    width = 180
                    print('', 26, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 26, '')
                    print()
                    print('', 27, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 27, '')
                    width = 95
                    print('', 28, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                        '                                '
                                                                        '                     ', 28, '')
                    width = 180
                    print('', 29, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 29, '')
                    width = 300
                    print('', 30, 'COMPOSITE NUMBERS(PRESS 4)                                         30'.center(width))
                    width = 180
                    print('', 31, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 31, '')
                    width = 93
                    number_seq = (input(" ".center(width)))

                    # SELECTING NUMBER SEQ. FROM ABOVE

                    # EVEN NUMBER.....
                    if number_seq == '1':
                        width = 180
                        print()
                        print('', 32, '---EVEN NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(1, limit + 1):
                                if i % 2 == 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(1, limit + 1):
                                if i % 2 == 0:
                                    print('', i, end=' ,')

                    # ODD NUMBER.....
                    elif number_seq == '2':
                        width = 180
                        print()
                        print('', 32, '---ODD NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(1, limit + 1):
                                if i % 2 != 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(1, limit + 1):
                                if i % 2 != 0:
                                    print('', i, end=' ,')


                    # PRIME NUMBERS.....
                    elif number_seq == '3':
                        width = 180
                        print()
                        print('', 32, '---PRIME NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            print(''.center(width), '2')
                            for i in range(1, limit + 1):
                                if i != 1 and i % 2 != 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            print('2 ,', end='')
                            for i in range(1, limit + 1):
                                if i != 1 and i % 2 != 0:
                                    print('', i, end=' ,')


                    # COMPOSITE NUMBERS.....
                    elif number_seq == '4':
                        width = 180
                        print()
                        print('', 32, '---COMPOSITE NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width), '',
                              33, '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(4, limit + 1):
                                if i % 2 == 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(4, limit + 1):
                                if i % 2 == 0:
                                    print('', i, end=' ,')


                    # FIBONACCHI NUMBERS.....
                    elif number_seq == '5':
                        width = 180
                        print()
                        print('', 32, '---FIBONACCHI NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width), '',
                              33, '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 25:
                            a, b = 1, 1
                            print(''.center(width), a)
                            print()
                            print(''.center(width), b)
                            print()
                            for i in range(limit - 2):
                                c = a + b
                                b = a
                                a = c
                                print(''.center(width), c, end='\n')
                                print()
                        elif limit > 25:
                            a, b = 1, 1
                            print(a, ',', end='')
                            print('', b, ',', end='')
                            for i in range(limit - 2):
                                c = a + b
                                b = a
                                a = c
                                print('', c, end=' ,')  # END OF WHAT TO DO 2

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER
                    width = 180
                    print()
                    print('', 34, ' DO YOU WANT TO PLAY WITH NUMBERS TOO?(yes or no)'.center(width), '', 34, '')
                    print()
                    width = 93
                    A_C = (input(" ".center(width)))
                    print()
                    if A_C == 'yes':
                        width = 180
                        print('', 35, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 35, '')

                        # 1st choice

                        msg = " 36"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   36\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # 2nd choice

                        msg = " 37"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   37\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print('', 38, ''.rjust(width), '', 38, '')

                        width = 92
                        CHOICE = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS CHOICES GIVEN
                        if CHOICE == '1':

                            # ALLEN ASSISTANT

                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, 'WELCOME TO MAGICA'.center(width), '', 40, '')
                            print('', 41, ''.rjust(width), '', 41, '')
                            print('', 42, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 42, '')
                            print('', 43, ''.rjust(width), '', 43, '')

                            width = 173
                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(
                                width)  # A 1ST LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN USER TALK:-
                            print()
                            USER = (input("      YOU-"))  # ALLEN USER TALK 1
                            print()
                            # /ALLEN USER TALK:-

                            # WHEN USER SAID YES
                            if USER == 'yes':  # when user said yes to allen

                                msg = " 46"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   46\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # ALLEN 3 DOTS

                                msg = " 47"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(' ALLEN-', end='')
                                msg = "......".ljust(width)  # A 4TH LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   47\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)  #

                                msg = " 48"  # ALLEN CONTINUES TO TALK
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   48\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                                msg = " 49"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                                    width)  # A 6TH LINE AND STEP 1
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   49\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 50"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(
                                    width)  # A 7TH LINE AND STEP 2
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   50\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                                    width)  # A 8TH LINE AND STEP 3
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(
                                    width)  # A 9TH LINE AND STEP 4
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                                    width)  # A 10TH LINE AND STEP 5
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                                    width)  # A 11TH LINE AND PART OF STEP 5
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                                    width)  # A 12TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 56"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                                    width)  # A 13TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                msg = "   56\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # ALLEN USER TALK:-
                                print()
                                USER_ANS = int(input("    YOUR ANS-"))
                                USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                                DIFF = USER_ANS - USER_ANS2
                                AGE = DIFF % 100
                                CHOOSEN_NO = DIFF // 100
                                print()
                                # /ALLEN USER TALK:-

                                msg = " 57"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(' ALLEN-', end='')
                                msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                                    width)  # A 14TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   57\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print()
                                print('    ALLEN- ', end='')
                                print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                                print(AGE, "YEARS")

                                print('    ALLEN- ', end='')
                                print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                                      end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                                print(CHOOSEN_NO)
                                print()

                                # END OF CHOICE= 1 WHEN USER SAY 'YES'
                                width = 180
                                print()
                                msg = " 58"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   58\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(59, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            # WHEN USER SAID NO
                            elif USER == 'no':  # when user said no to allen

                                msg = " 46"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   46\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 47"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   47\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # OFFERING 2ND CHOICE TO USER.................................
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 49, '')
                                print('', 50, 'WELCOME TO PATTERNS'.center(width), '', 50, '')
                                print('', 51, ''.rjust(width), '', 51, '')
                                print('', 52, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 52, '')
                                print('', 53, ''.rjust(width), '', 53, '')
                                print('', 54, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 54, '')
                                print('', 55, ''.center(width), '', 55, '')
                                print('', 56, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 56, '')
                                width = 92
                                PATTERN = (input(" ".center(width)))

                                # SELECTING FROM VARIOUS PATTERNS......1
                                if PATTERN == '1':
                                    width = 180
                                    print('', 57, ''.rjust(width), '', 57, '')
                                    print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                                    print('', 59, ''.rjust(width), '', 59, '')

                                    print('', 60, '* RECTANGLE'.ljust(width), '', 60, '')  # RECTANGLE IS MADE HERE
                                    l = int(input("       ENTER LENGTH:"))
                                    b = int(input("       ENTER BREADTH:"))
                                    for i in range(1, l + 1):
                                        for j in range(1, b + 1):
                                            if i == 1 or i == l or j == 1 or j == b:

                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()

                                    print('', 61, '* SQUARE'.ljust(width), '', 61, '')  # SQUARE IS MADE HERE
                                    # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                    n = int(input("       ENTER SIDE:"))
                                    for i in range(1, n + 1):
                                        for j in range(1, n + 1):
                                            if i == 1 or i == n or j == 1 or j == n:
                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()

                                    print('', 62, '* CIRCLE'.ljust(width), '', 62, '')  # CIRCLE IS MADE HERE
                                    row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                    col = row
                                    for i in range(row):
                                        for j in range(col):
                                            if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                    i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                    j == 1 or j == col - 2) or i == row - 2 and (
                                                    j == 1 or j == col - 2):
                                                print('*',
                                                      end=' ')  # end='' so that print statement should not change the line.

                                            else:
                                                print(' ', end=' ')  # to print the space.
                                        print()  # to change the line after iteration of inner loop.

                                    print('', 63, '* TRIANGLE'.ljust(width), '', 63, '')  # TRIANGLE IS MADE HERE
                                    n = int(input("       ENTER HEIGHT:"))
                                    for row in range(1, n + 1):
                                        for col in range(1, 2 * n):
                                            if row == n or row + col == n + 1 or col - row == n - 1:
                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()



                                # SELECTING FROM VARIOUS PATTERNS......2
                                elif PATTERN == '2':
                                    width = 180
                                    print('', 57, ''.rjust(width), '', 57, '')
                                    print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                                    print('', 59, ''.rjust(width), '', 59, '')

                                    # URSA MAJOR HEADING
                                    msg = " 60"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- URSA MAJOR ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   60\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 160  # URSA MAJOR PATTERN
                                    print('*'.center(width))
                                    width = 170
                                    print('*'.center(width))
                                    width = 175
                                    print('*'.center(width))
                                    print()
                                    width = 185
                                    print('*'.center(width))
                                    width = 205
                                    print('*'.center(width))
                                    width = 188
                                    print('*'.center(width))
                                    width = 200
                                    print('*'.center(width))  # /URSA MAJOR PATTERN
                                    print()
                                    print()

                                    # URSA MINOR HEADING
                                    width = 180
                                    msg = " 61"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- URSA MINOR ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   61\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 200  # URSA MINOR PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 190
                                    print('*'.center(width))
                                    print()
                                    width = 185
                                    print('*'.center(width))
                                    for i in range(1, 4):
                                        print()
                                    width = 188
                                    print('*'.center(width))
                                    width = 175
                                    print('*'.center(width))
                                    print()
                                    print()
                                    width = 193
                                    print('*'.center(width))
                                    width = 183
                                    print('*'.center(width))  # /URSA MINOR PATTERN
                                    print()
                                    print()

                                    # ORION HEADING
                                    width = 180
                                    msg = " 62"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- ORION ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   62\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 200  # ORION PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 170
                                    print('*'.center(width))
                                    print()
                                    width = 210
                                    print('*'.center(width))
                                    for i in range(1, 7):
                                        print()

                                    width = 193
                                    print('*'.center(width))
                                    width = 188
                                    print('*'.center(width))
                                    width = 182
                                    print('*'.center(width))
                                    for i in range(1, 7):
                                        print()
                                    width = 210
                                    print('*'.center(width))
                                    width = 168
                                    print('*'.center(width))  # /ORION PATTERN
                                    print()
                                    print()

                                    # CASSIOPEIA HEADING
                                    width = 180
                                    msg = " 63"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- CASSIOPEIA ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   63\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 210  # CASSIOPEIA PATTERN
                                    print('*'.center(width))
                                    print()
                                    print()
                                    width = 180
                                    print('*'.center(width))
                                    width = 207
                                    print('*'.center(width))
                                    width = 140
                                    print('*'.center(width))
                                    width = 173
                                    print('*'.center(width))  # /CASSIOPEIA PATTERN
                                    print()
                                    print()

                                    # ARIES HEADING
                                    width = 180
                                    msg = " 64"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- ARIES ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   64\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 180  # ARIES PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 200
                                    print('*'.center(width))
                                    width = 207
                                    print('*'.center(width))
                                    width = 205
                                    print('*'.center(width))  # /ARIES PATTERN
                                    print()

                                    # END OF CHOICE= 2
                                    width = 180
                                    print()
                                    msg = " 64"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   64\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    for i in range(65, 71):
                                        print('', i, ''.rjust(width), '', i, '')

                            # END OF CHOICE= 1 WHEN USER SAY 'NO'





                        # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                        elif CHOICE == '2':
                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                            print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                            print('', 42, ''.rjust(width), '', 42, '')
                            print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                            print('', 44, ''.rjust(width), '', 44, '')
                            print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                            print('', 46, ''.center(width), '', 46, '')
                            print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                            width = 92
                            PATTERN = (input(" ".center(width)))

                            # SELECTING FROM VARIOUS PATTERNS......1
                            if PATTERN == '1':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                                l = int(input("       ENTER LENGTH:"))
                                b = int(input("       ENTER BREADTH:"))
                                for i in range(1, l + 1):
                                    for j in range(1, b + 1):
                                        if i == 1 or i == l or j == 1 or j == b:

                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                                # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                n = int(input("       ENTER SIDE:"))
                                for i in range(1, n + 1):
                                    for j in range(1, n + 1):
                                        if i == 1 or i == n or j == 1 or j == n:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                                row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                col = row
                                for i in range(row):
                                    for j in range(col):
                                        if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                            print('*',
                                                  end=' ')  # end='' so that print statement should not change the line.

                                        else:
                                            print(' ', end=' ')  # to print the space.
                                    print()  # to change the line after iteration of inner loop.

                                print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                                n = int(input("       ENTER HEIGHT:"))
                                for row in range(1, n + 1):
                                    for col in range(1, 2 * n):
                                        if row == n or row + col == n + 1 or col - row == n - 1:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()



                            # SELECTING FROM VARIOUS PATTERNS......2
                            elif PATTERN == '2':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                # URSA MAJOR HEADING
                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MAJOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 160  # URSA MAJOR PATTERN
                                print('*'.center(width))
                                width = 170
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 200
                                print('*'.center(width))  # /URSA MAJOR PATTERN
                                print()
                                print()

                                # URSA MINOR HEADING
                                width = 180
                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MINOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # URSA MINOR PATTERN
                                print('*'.center(width))
                                print()
                                width = 190
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                for i in range(1, 4):
                                    print()
                                width = 188
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                print()
                                width = 193
                                print('*'.center(width))
                                width = 183
                                print('*'.center(width))  # /URSA MINOR PATTERN
                                print()
                                print()

                                # ORION HEADING
                                width = 180
                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ORION ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # ORION PATTERN
                                print('*'.center(width))
                                print()
                                width = 170
                                print('*'.center(width))
                                print()
                                width = 210
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()

                                width = 193
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 182
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()
                                width = 210
                                print('*'.center(width))
                                width = 168
                                print('*'.center(width))  # /ORION PATTERN
                                print()
                                print()

                                # CASSIOPEIA HEADING
                                width = 180
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- CASSIOPEIA ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 210  # CASSIOPEIA PATTERN
                                print('*'.center(width))
                                print()
                                print()
                                width = 180
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 140
                                print('*'.center(width))
                                width = 173
                                print('*'.center(width))  # /CASSIOPEIA PATTERN
                                print()
                                print()

                                # ARIES HEADING
                                width = 180
                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ARIES ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 180  # ARIES PATTERN
                                print('*'.center(width))
                                print()
                                width = 200
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))  # /ARIES PATTERN
                                print()

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(56, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                # MORE  ABOVE CODING  OF PLAY WITH NUMBERS..........................................................


                    elif A_C == 'no':
                        width = 180
                        print()
                        print('', 35, 'OK BYE'.center(width), '', 35, '')
                        print('', 36, 'ENJOY YOUR DAY :)'.center(width), '', 36, '')
                        for i in range(37, 51):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''

                #......................................................................


            #IF  2ND ANS. IS WRONG'''
            else:
                print()
                print('', 23, ''.rjust(width), '', 23, '')
                print('', 24, '|OHH SORRY! YOU ARE AGAIN WRONG|'.center(width), '', 24, '')
                print('', 25, 'OKK BYE :)'.center(width), '', 25, '')
                for i in range(26, 31):
                    print('', i, ''.rjust(width), '', i, '')

        #IF THE USER DENIES'''
        elif C == 'no':
            width = 180
            print()
            print('', 21, 'OKK BYE :)'.center(width), '', 21, '')
            for i in range(22, 31):
                print('', i, ''.rjust(width), '', i, '')


#QUESTION 1 STARTS ON ANSWERING NO ABOVE'''# question 1
elif E == 'no':
    width = 180
    print('', 13, ' OK SO ANSWER IT ONLY:-'.center(width), '', 13, '')
    print('', 14, ''.rjust(width), '', 14, '')
    width = 85
    A = (input(" ".center(width)))
    width = 180
    B = 'i ate some pie'

    '''WHEN THE ANSWER IS CORRECT(i ate some pie)'''
    if A == B:
        print('', 15, ''.rjust(width), '', 15, '')
        print('', 16, 'YOU GOT SOME CHILLS...HUHH!'.center(width), '', 16, '')
        print('', 17, ''.rjust(width), '', 17, '')
        print('', 18, '|YOU ARE SUCCESSFULLY LOGGED IN|'.center(width), '', 18, '')
        print('', 19, '| SO: |'.center(width), '', 19, '')
        print('', 20, ''.rjust(width), '', 20, '')

        # MAIN TOPIC STARTS FROM HERE I.E. WHAT TO DO WITH NUMBERS

        print('', 21, ''.rjust(width), '', 21, '')
        print('', 22, 'NOW SELECT WHAT DO YOU WANT TO DO WITH NUMBERS'.center(width), '', 22, '')
        print('', 23, 'PLAY WITH NUMBERS(PRESS 1)'.ljust(width), '', 23, '')
        print('', 24, 'OR'.center(width), '', 24, '')
        print('', 25, 'FIND OUT VARIOUS NUMBER SEQUENCE(PRESS 2)'.rjust(width), '', 25, '')
        width = 93
        WHATTODO = (input(" ".center(width)))

        # PLAY WITH NUMBERS LOOP START FROM HERE WITH 2 CHOICES

        # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 1)
        if WHATTODO == '1':
            width = 180
            print('', 26, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 26, '')

            # 1st choice

            msg = " 27"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "   27\n"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)

            # 2nd choice

            msg = " 28"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
            msg = "   28\n"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)

            print('', 29, ''.rjust(width), '', 29, '')

            width = 92
            CHOICE = (input(" ".center(width)))

            # SELECTING FROM VARIOUS CHOICES GIVEN
            if CHOICE == '1':

                # ALLEN ASSISTANT

                width = 180
                print('', 30, ''.rjust(width), '', 30, '')
                print('', 31, 'WELCOME TO MAGICA'.center(width), '', 31, '')
                print('', 32, ''.rjust(width), '', 32, '')
                print('', 33, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 33, '')
                print('', 34, ''.rjust(width), '', 34, '')

                width = 173
                msg = " 35"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print(' ALLEN-', end='')
                msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   35\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                msg = " 36"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print(' ALLEN-', end='')
                msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   36\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                # ALLEN USER TALK:-
                print()
                USER = (input("      YOU-"))  # ALLEN USER TALK 1
                print()
                # /ALLEN USER TALK:-

                # WHEN USER SAID YES
                if USER == 'yes':  # when user said yes to allen

                    msg = " 37"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   37\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # ALLEN 3 DOTS

                    msg = " 38"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print(' ALLEN-', end='')
                    msg = "......".ljust(width)  # A 4TH LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   38\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)  #

                    msg = " 39"  # ALLEN CONTINUES TO TALK
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   39\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                    msg = " 40"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                        width)  # A 6TH LINE AND STEP 1
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   40\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 41"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(width)  # A 7TH LINE AND STEP 2
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   41\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 42"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                        width)  # A 8TH LINE AND STEP 3
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   42\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 43"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   43\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                        width)  # A 10TH LINE AND STEP 5
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                        width)  # A 11TH LINE AND PART OF STEP 5
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 46"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                        width)  # A 12TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    msg = "   46\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 47"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                        width)  # A 13TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    msg = "   47\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # ALLEN USER TALK:-
                    print()
                    USER_ANS = int(input("    YOUR ANS-"))
                    USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                    DIFF = USER_ANS - USER_ANS2
                    AGE = DIFF % 100
                    CHOOSEN_NO = DIFF // 100
                    print()
                    # /ALLEN USER TALK:-

                    msg = " 48"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print(' ALLEN-', end='')
                    msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                        width)  # A 14TH LINE ( SIMPLE TALK)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   48\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.1)

                    print()
                    print('    ALLEN- ', end='')
                    print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                    print(AGE, "YEARS")

                    print('    ALLEN- ', end='')
                    print("AND THE NUMBER YOU HAVE CHOOSEN IS: ", end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                    print(CHOOSEN_NO)
                    print()

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 49, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 49, '')
                    print()
                    width = 93
                    A_C2 = (input(" ".center(width)))
                    print()
                    if A_C2 == 'yes':
                        width = 180
                        print('', 50, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 50, '')
                        print()
                        print('', 51, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 51, '')
                        width = 95
                        print('', 52, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 52, '')
                        width = 180
                        print('', 53, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 53, '')
                        width = 300
                        print('', 54,
                              'COMPOSITE NUMBERS(PRESS 4)                                         54'.center(width))
                        width = 180
                        print('', 55, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 55, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 56, '---EVEN NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 56, '---ODD NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 56, '---PRIME NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 56, '---COMPOSITE NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 56, '---FIBONACCHI NUMBERS---'.center(width), '', 56, '')
                            print()
                            print('', 57,
                                  'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 57, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                        '''END OF WHATTODO=2'''

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 58"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   58\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(59, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif A_C2 == 'no':
                        width = 180
                        print()
                        print('', 49, 'OK BYE'.center(width), '', 49, '')
                        print('', 50, 'ENJOY YOUR DAY :)'.center(width), '', 50, '')
                        for i in range(51, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''MAGIC YES FINALLY FINISHED'''

                # WHEN USER SAID NO
                elif USER == 'no':  # when user said no to allen

                    msg = " 37"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   37\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 38"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   38\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # OFFERING 2ND CHOICE TO USER.................................
                    width = 180
                    print('', 39, ''.rjust(width), '', 39, '')
                    print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                    print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                    print('', 42, ''.rjust(width), '', 42, '')
                    print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                    print('', 44, ''.rjust(width), '', 44, '')
                    print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                    print('', 46, ''.center(width), '', 46, '')
                    print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                    width = 92
                    PATTERN = (input(" ".center(width)))

                    # SELECTING FROM VARIOUS PATTERNS......1
                    if PATTERN == '1':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                        l = int(input("       ENTER LENGTH:"))
                        b = int(input("       ENTER BREADTH:"))
                        for i in range(1, l + 1):
                            for j in range(1, b + 1):
                                if i == 1 or i == l or j == 1 or j == b:

                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                        # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                        n = int(input("       ENTER SIDE:"))
                        for i in range(1, n + 1):
                            for j in range(1, n + 1):
                                if i == 1 or i == n or j == 1 or j == n:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                        row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                        col = row
                        for i in range(row):
                            for j in range(col):
                                if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                        i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                        j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                    print('*', end=' ')  # end='' so that print statement should not change the line.

                                else:
                                    print(' ', end=' ')  # to print the space.
                            print()  # to change the line after iteration of inner loop.

                        print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                        n = int(input("       ENTER HEIGHT:"))
                        for row in range(1, n + 1):
                            for col in range(1, 2 * n):
                                if row == n or row + col == n + 1 or col - row == n - 1:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()



                    # SELECTING FROM VARIOUS PATTERNS......2
                    elif PATTERN == '2':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        # URSA MAJOR HEADING
                        msg = " 51"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MAJOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   51\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 160  # URSA MAJOR PATTERN
                        print('*'.center(width))
                        width = 170
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 200
                        print('*'.center(width))  # /URSA MAJOR PATTERN
                        print()
                        print()

                        # URSA MINOR HEADING
                        width = 180
                        msg = " 52"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MINOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   52\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # URSA MINOR PATTERN
                        print('*'.center(width))
                        print()
                        width = 190
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        for i in range(1, 4):
                            print()
                        width = 188
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        print()
                        width = 193
                        print('*'.center(width))
                        width = 183
                        print('*'.center(width))  # /URSA MINOR PATTERN
                        print()
                        print()

                        # ORION HEADING
                        width = 180
                        msg = " 53"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ORION ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   53\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # ORION PATTERN
                        print('*'.center(width))
                        print()
                        width = 170
                        print('*'.center(width))
                        print()
                        width = 210
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()

                        width = 193
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 182
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()
                        width = 210
                        print('*'.center(width))
                        width = 168
                        print('*'.center(width))  # /ORION PATTERN
                        print()
                        print()

                        # CASSIOPEIA HEADING
                        width = 180
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- CASSIOPEIA ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 210  # CASSIOPEIA PATTERN
                        print('*'.center(width))
                        print()
                        print()
                        width = 180
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 140
                        print('*'.center(width))
                        width = 173
                        print('*'.center(width))  # /CASSIOPEIA PATTERN
                        print()
                        print()

                        # ARIES HEADING
                        width = 180
                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ARIES ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 180  # ARIES PATTERN
                        print('*'.center(width))
                        print()
                        width = 200
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))  # /ARIES PATTERN
                        print()

                    # END OF CHOICE= 1 WHEN USER SAY 'NO'

                    '''END OF WHATTODO 1'''

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 55, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 55, '')
                    print()
                    width = 93
                    A_C2 = (input(" ".center(width)))
                    print()
                    if A_C2 == 'yes':
                        width = 180
                        print('', 56, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 56, '')
                        print()
                        print('', 57, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 57, '')
                        width = 95
                        print('', 58, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 58, '')
                        width = 180
                        print('', 59, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 59, '')
                        width = 300
                        print('', 60,
                              'COMPOSITE NUMBERS(PRESS 4)                                         60'.center(width))
                        width = 180
                        print('', 61, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 61, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 62, '---EVEN NUMBERS---'.center(width), '', 62, '')
                            print()
                            print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  63, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 62, '---ODD NUMBERS---'.center(width), '', 62, '')
                            print()
                            print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  63, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 62, '---PRIME NUMBERS---'.center(width), '', 62, '')
                            print()
                            print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  63, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 62, '---COMPOSITE NUMBERS---'.center(width), '', 62, '')
                            print()
                            print('', 63, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 63, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 62, '---FIBONACCHI NUMBERS---'.center(width), '', 62, '')
                            print()
                            print('', 63,
                                  'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 63, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                            '''END OF WHATTODO=2'''

                            # END OF CHOICE= 2
                            width = 180
                            print()
                            msg = " 64"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   64\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            for i in range(65, 71):
                                print('', i, ''.rjust(width), '', i, '')

                    elif A_C2 == 'no':
                        width = 180
                        print()
                        print('', 55, 'OK BYE'.center(width), '', 55, '')
                        print('', 56, 'ENJOY YOUR DAY :)'.center(width), '', 56, '')
                        for i in range(57, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''




            # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
            elif CHOICE == '2':
                width = 180
                print('', 30, ''.rjust(width), '', 30, '')
                print('', 31, 'WELCOME TO PATTERNS'.center(width), '', 31, '')
                print('', 32, ''.rjust(width), '', 32, '')
                print('', 33, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 33, '')
                print('', 34, ''.rjust(width), '', 34, '')
                print('', 35, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 35, '')
                print('', 36, ''.center(width), '', 36, '')
                print('', 37, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 37, '')
                width = 92
                PATTERN = (input(" ".center(width)))

                # SELECTING FROM VARIOUS PATTERNS......1
                if PATTERN == '1':
                    width = 180
                    print('', 38, ''.rjust(width), '', 38, '')
                    print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                    print('', 40, ''.rjust(width), '', 40, '')

                    print('', 41, '* RECTANGLE'.ljust(width), '', 41, '')  # RECTANGLE IS MADE HERE
                    l = int(input("       ENTER LENGTH:"))
                    b = int(input("       ENTER BREADTH:"))
                    for i in range(1, l + 1):
                        for j in range(1, b + 1):
                            if i == 1 or i == l or j == 1 or j == b:

                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()

                    print('', 42, '* SQUARE'.ljust(width), '', 42, '')  # SQUARE IS MADE HERE
                    # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                    n = int(input("       ENTER SIDE:"))
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if i == 1 or i == n or j == 1 or j == n:
                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()

                    print('', 43, '* CIRCLE'.ljust(width), '', 43, '')  # CIRCLE IS MADE HERE
                    row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                    col = row
                    for i in range(row):
                        for j in range(col):
                            if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                    i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                    j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                print('*', end=' ')  # end='' so that print statement should not change the line.

                            else:
                                print(' ', end=' ')  # to print the space.
                        print()  # to change the line after iteration of inner loop.

                    print('', 44, '* TRIANGLE'.ljust(width), '', 44, '')  # TRIANGLE IS MADE HERE
                    n = int(input("       ENTER HEIGHT:"))
                    for row in range(1, n + 1):
                        for col in range(1, 2 * n):
                            if row == n or row + col == n + 1 or col - row == n - 1:
                                print('*', end=' ')
                            else:
                                print(' ', end=' ')
                        print()

                    '''END OF WHATTODO 1'''

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45, '')
                    print()
                    width = 93
                    AC = (input(" ".center(width)))
                    print()
                    if AC == 'yes':
                        width = 180
                        print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                        print()
                        print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                        width = 95
                        print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 48, '')
                        width = 180
                        print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                        width = 300
                        print('', 50,
                              'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(width))
                        width = 180
                        print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                            '''END OF WHATTODO=2'''

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(55, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif AC == 'no':
                        width = 180
                        print()
                        print('', 46, 'OK BYE'.center(width), '', 46, '')
                        print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                        for i in range(48, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''


                # SELECTING FROM VARIOUS PATTERNS......2
                elif PATTERN == '2':
                    width = 180
                    print('', 38, ''.rjust(width), '', 38, '')
                    print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                    print('', 40, ''.rjust(width), '', 40, '')

                    # URSA MAJOR HEADING
                    msg = " 41"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- URSA MAJOR ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   41\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 160  # URSA MAJOR PATTERN
                    print('*'.center(width))
                    width = 170
                    print('*'.center(width))
                    width = 175
                    print('*'.center(width))
                    print()
                    width = 185
                    print('*'.center(width))
                    width = 205
                    print('*'.center(width))
                    width = 188
                    print('*'.center(width))
                    width = 200
                    print('*'.center(width))  # /URSA MAJOR PATTERN
                    print()
                    print()

                    # URSA MINOR HEADING
                    width = 180
                    msg = " 42"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- URSA MINOR ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   42\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 200  # URSA MINOR PATTERN
                    print('*'.center(width))
                    print()
                    width = 190
                    print('*'.center(width))
                    print()
                    width = 185
                    print('*'.center(width))
                    for i in range(1, 4):
                        print()
                    width = 188
                    print('*'.center(width))
                    width = 175
                    print('*'.center(width))
                    print()
                    print()
                    width = 193
                    print('*'.center(width))
                    width = 183
                    print('*'.center(width))  # /URSA MINOR PATTERN
                    print()
                    print()

                    # ORION HEADING
                    width = 180
                    msg = " 43"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- ORION ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   43\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 200  # ORION PATTERN
                    print('*'.center(width))
                    print()
                    width = 170
                    print('*'.center(width))
                    print()
                    width = 210
                    print('*'.center(width))
                    for i in range(1, 7):
                        print()

                    width = 193
                    print('*'.center(width))
                    width = 188
                    print('*'.center(width))
                    width = 182
                    print('*'.center(width))
                    for i in range(1, 7):
                        print()
                    width = 210
                    print('*'.center(width))
                    width = 168
                    print('*'.center(width))  # /ORION PATTERN
                    print()
                    print()

                    # CASSIOPEIA HEADING
                    width = 180
                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- CASSIOPEIA ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 210  # CASSIOPEIA PATTERN
                    print('*'.center(width))
                    print()
                    print()
                    width = 180
                    print('*'.center(width))
                    width = 207
                    print('*'.center(width))
                    width = 140
                    print('*'.center(width))
                    width = 173
                    print('*'.center(width))  # /CASSIOPEIA PATTERN
                    print()
                    print()

                    # ARIES HEADING
                    width = 180
                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "---- ARIES ----".center(width)
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print()
                    width = 180  # ARIES PATTERN
                    print('*'.center(width))
                    print()
                    width = 200
                    print('*'.center(width))
                    width = 207
                    print('*'.center(width))
                    width = 205
                    print('*'.center(width))  # /ARIES PATTERN
                    print()

                    '''END OF WHATTODO 1'''

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                    width = 180
                    print()
                    print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45, '')
                    print()
                    width = 93
                    AC = (input(" ".center(width)))
                    print()
                    if AC == 'yes':
                        width = 180
                        print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                        print()
                        print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                        width = 95
                        print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                            '                                '
                                                                            '                     ', 48, '')
                        width = 180
                        print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                        width = 300
                        print('', 50,
                              'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(width))
                        width = 180
                        print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                        width = 93
                        number_seq = (input(" ".center(width)))

                        # SELECTING NUMBER SEQ. FROM ABOVE

                        # EVEN NUMBER.....
                        if number_seq == '1':
                            width = 180
                            print()
                            print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')

                        # ODD NUMBER.....
                        elif number_seq == '2':
                            width = 180
                            print()
                            print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(1, limit + 1):
                                    if i % 2 != 0:
                                        print('', i, end=' ,')


                        # PRIME NUMBERS.....
                        elif number_seq == '3':
                            width = 180
                            print()
                            print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                  53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                print(''.center(width), '2')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                print('2 ,', end='')
                                for i in range(1, limit + 1):
                                    if i != 1 and i % 2 != 0:
                                        print('', i, end=' ,')


                        # COMPOSITE NUMBERS.....
                        elif number_seq == '4':
                            width = 180
                            print()
                            print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print(''.center(width), i, end=' ')
                                    print()
                            elif limit > 50:
                                for i in range(4, limit + 1):
                                    if i % 2 == 0:
                                        print('', i, end=' ,')


                        # FIBONACCHI NUMBERS.....
                        elif number_seq == '5':
                            width = 180
                            print()
                            print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                            print()
                            print('', 53, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                  '', 53, '')
                            width = 93
                            limit = int(input(" ".center(width)))
                            print()
                            if limit <= 25:
                                a, b = 1, 1
                                print(''.center(width), a)
                                print()
                                print(''.center(width), b)
                                print()
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print(''.center(width), c, end='\n')
                                    print()
                            elif limit > 25:
                                a, b = 1, 1
                                print(a, ',', end='')
                                print('', b, ',', end='')
                                for i in range(limit - 2):
                                    c = a + b
                                    b = a
                                    a = c
                                    print('', c, end=' ,')

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(55, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    elif AC == 'no':
                        width = 180
                        print()
                        print('', 46, 'OK BYE'.center(width), '', 46, '')
                        print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                        for i in range(48, 61):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''



        # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 2)
        elif WHATTODO == '2':
            width = 180
            print('', 26, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 26, '')
            print()
            print('', 27, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 27, '')
            width = 95
            print('', 28, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                '                                '
                                                                '                     ', 28, '')
            width = 180
            print('', 29, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 29, '')
            width = 300
            print('', 30, 'COMPOSITE NUMBERS(PRESS 4)                                         30'.center(width))
            width = 180
            print('', 31, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 31, '')
            width = 93
            number_seq = (input(" ".center(width)))

            # SELECTING NUMBER SEQ. FROM ABOVE

            # EVEN NUMBER.....
            if number_seq == '1':
                width = 180
                print()
                print('', 32, '---EVEN NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(1, limit + 1):
                        if i % 2 == 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(1, limit + 1):
                        if i % 2 == 0:
                            print('', i, end=' ,')

            # ODD NUMBER.....
            elif number_seq == '2':
                width = 180
                print()
                print('', 32, '---ODD NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(1, limit + 1):
                        if i % 2 != 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(1, limit + 1):
                        if i % 2 != 0:
                            print('', i, end=' ,')


            # PRIME NUMBERS.....
            elif number_seq == '3':
                width = 180
                print()
                print('', 32, '---PRIME NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    print(''.center(width), '2')
                    for i in range(1, limit + 1):
                        if i != 1 and i % 2 != 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    print('2 ,', end='')
                    for i in range(1, limit + 1):
                        if i != 1 and i % 2 != 0:
                            print('', i, end=' ,')


            # COMPOSITE NUMBERS.....
            elif number_seq == '4':
                width = 180
                print()
                print('', 32, '---COMPOSITE NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 50:
                    for i in range(4, limit + 1):
                        if i % 2 == 0:
                            print(''.center(width), i, end=' ')
                        print()
                elif limit > 50:
                    for i in range(4, limit + 1):
                        if i % 2 == 0:
                            print('', i, end=' ,')


            # FIBONACCHI NUMBERS.....
            elif number_seq == '5':
                width = 180
                print()
                print('', 32, '---FIBONACCHI NUMBERS---'.center(width), '', 32, '')
                print()
                print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width), '', 33, '')
                width = 93
                limit = int(input(" ".center(width)))
                print()
                if limit <= 25:
                    a, b = 1, 1
                    print(''.center(width), a)
                    print()
                    print(''.center(width), b)
                    print()
                    for i in range(limit - 2):
                        c = a + b
                        b = a
                        a = c
                        print(''.center(width), c, end='\n')
                        print()
                elif limit > 25:
                    a, b = 1, 1
                    print(a, ',', end='')
                    print('', b, ',', end='')
                    for i in range(limit - 2):
                        c = a + b
                        b = a
                        a = c
                        print('', c, end=' ,')  # END OF WHAT TO DO 2

            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER
            width = 180
            print()
            print('', 34, ' DO YOU WANT TO PLAY WITH NUMBERS TOO?(yes or no)'.center(width), '', 34, '')
            print()
            width = 93
            A_C = (input(" ".center(width)))
            print()
            if A_C == 'yes':
                width = 180
                print('', 35, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 35, '')

                # 1st choice

                msg = " 36"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   36\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                # 2nd choice

                msg = " 37"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   37\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)

                print('', 38, ''.rjust(width), '', 38, '')

                width = 92
                CHOICE = (input(" ".center(width)))

                # SELECTING FROM VARIOUS CHOICES GIVEN
                if CHOICE == '1':

                    # ALLEN ASSISTANT

                    width = 180
                    print('', 39, ''.rjust(width), '', 39, '')
                    print('', 40, 'WELCOME TO MAGICA'.center(width), '', 40, '')
                    print('', 41, ''.rjust(width), '', 41, '')
                    print('', 42, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 42, '')
                    print('', 43, ''.rjust(width), '', 43, '')

                    width = 173
                    msg = " 44"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   44\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    msg = " 45"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    print(' ALLEN-', end='')
                    msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   45\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # ALLEN USER TALK:-
                    print()
                    USER = (input("      YOU-"))  # ALLEN USER TALK 1
                    print()
                    # /ALLEN USER TALK:-

                    # WHEN USER SAID YES
                    if USER == 'yes':  # when user said yes to allen

                        msg = " 46"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   46\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN 3 DOTS

                        msg = " 47"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print(' ALLEN-', end='')
                        msg = "......".ljust(width)  # A 4TH LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   47\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)  #

                        msg = " 48"  # ALLEN CONTINUES TO TALK
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   48\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                        msg = " 49"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                            width)  # A 6TH LINE AND STEP 1
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   49\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 50"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(width)  # A 7TH LINE AND STEP 2
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   50\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 51"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                            width)  # A 8TH LINE AND STEP 3
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   51\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 52"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   52\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 53"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                            width)  # A 10TH LINE AND STEP 5
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   53\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                            width)  # A 11TH LINE AND PART OF STEP 5
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                            width)  # A 12TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 56"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                            width)  # A 13TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        msg = "   56\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN USER TALK:-
                        print()
                        USER_ANS = int(input("    YOUR ANS-"))
                        USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                        DIFF = USER_ANS - USER_ANS2
                        AGE = DIFF % 100
                        CHOOSEN_NO = DIFF // 100
                        print()
                        # /ALLEN USER TALK:-

                        msg = " 57"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print(' ALLEN-', end='')
                        msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                            width)  # A 14TH LINE ( SIMPLE TALK)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   57\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print()
                        print('    ALLEN- ', end='')
                        print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                        print(AGE, "YEARS")

                        print('    ALLEN- ', end='')
                        print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                              end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                        print(CHOOSEN_NO)
                        print()

                        # END OF CHOICE= 1 WHEN USER SAY 'YES'
                        width = 180
                        print()
                        msg = " 58"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   58\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(59, 61):
                            print('', i, ''.rjust(width), '', i, '')

                    # WHEN USER SAID NO
                    elif USER == 'no':  # when user said no to allen

                        msg = " 46"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   46\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 47"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   47\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # OFFERING 2ND CHOICE TO USER.................................
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 49, '')
                        print('', 50, 'WELCOME TO PATTERNS'.center(width), '', 50, '')
                        print('', 51, ''.rjust(width), '', 51, '')
                        print('', 52, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 52, '')
                        print('', 53, ''.rjust(width), '', 53, '')
                        print('', 54, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 54, '')
                        print('', 55, ''.center(width), '', 55, '')
                        print('', 56, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 56, '')
                        width = 92
                        PATTERN = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS PATTERNS......1
                        if PATTERN == '1':
                            width = 180
                            print('', 57, ''.rjust(width), '', 57, '')
                            print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                            print('', 59, ''.rjust(width), '', 59, '')

                            print('', 60, '* RECTANGLE'.ljust(width), '', 60, '')  # RECTANGLE IS MADE HERE
                            l = int(input("       ENTER LENGTH:"))
                            b = int(input("       ENTER BREADTH:"))
                            for i in range(1, l + 1):
                                for j in range(1, b + 1):
                                    if i == 1 or i == l or j == 1 or j == b:

                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 61, '* SQUARE'.ljust(width), '', 61, '')  # SQUARE IS MADE HERE
                            # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                            n = int(input("       ENTER SIDE:"))
                            for i in range(1, n + 1):
                                for j in range(1, n + 1):
                                    if i == 1 or i == n or j == 1 or j == n:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 62, '* CIRCLE'.ljust(width), '', 62, '')  # CIRCLE IS MADE HERE
                            row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                            col = row
                            for i in range(row):
                                for j in range(col):
                                    if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                            i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                            j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                        print('*',
                                              end=' ')  # end='' so that print statement should not change the line.

                                    else:
                                        print(' ', end=' ')  # to print the space.
                                print()  # to change the line after iteration of inner loop.

                            print('', 63, '* TRIANGLE'.ljust(width), '', 63, '')  # TRIANGLE IS MADE HERE
                            n = int(input("       ENTER HEIGHT:"))
                            for row in range(1, n + 1):
                                for col in range(1, 2 * n):
                                    if row == n or row + col == n + 1 or col - row == n - 1:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()



                        # SELECTING FROM VARIOUS PATTERNS......2
                        elif PATTERN == '2':
                            width = 180
                            print('', 57, ''.rjust(width), '', 57, '')
                            print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                            print('', 59, ''.rjust(width), '', 59, '')

                            # URSA MAJOR HEADING
                            msg = " 60"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MAJOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   60\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 160  # URSA MAJOR PATTERN
                            print('*'.center(width))
                            width = 170
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 200
                            print('*'.center(width))  # /URSA MAJOR PATTERN
                            print()
                            print()

                            # URSA MINOR HEADING
                            width = 180
                            msg = " 61"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MINOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   61\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # URSA MINOR PATTERN
                            print('*'.center(width))
                            print()
                            width = 190
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            for i in range(1, 4):
                                print()
                            width = 188
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            print()
                            width = 193
                            print('*'.center(width))
                            width = 183
                            print('*'.center(width))  # /URSA MINOR PATTERN
                            print()
                            print()

                            # ORION HEADING
                            width = 180
                            msg = " 62"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ORION ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   62\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # ORION PATTERN
                            print('*'.center(width))
                            print()
                            width = 170
                            print('*'.center(width))
                            print()
                            width = 210
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()

                            width = 193
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 182
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()
                            width = 210
                            print('*'.center(width))
                            width = 168
                            print('*'.center(width))  # /ORION PATTERN
                            print()
                            print()

                            # CASSIOPEIA HEADING
                            width = 180
                            msg = " 63"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- CASSIOPEIA ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   63\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 210  # CASSIOPEIA PATTERN
                            print('*'.center(width))
                            print()
                            print()
                            width = 180
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 140
                            print('*'.center(width))
                            width = 173
                            print('*'.center(width))  # /CASSIOPEIA PATTERN
                            print()
                            print()

                            # ARIES HEADING
                            width = 180
                            msg = " 64"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ARIES ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   64\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 180  # ARIES PATTERN
                            print('*'.center(width))
                            print()
                            width = 200
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))  # /ARIES PATTERN
                            print()

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 64"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   64\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(65, 71):
                            print('', i, ''.rjust(width), '', i, '')

                    # END OF CHOICE= 1 WHEN USER SAY 'NO'





                # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                elif CHOICE == '2':
                    width = 180
                    print('', 39, ''.rjust(width), '', 39, '')
                    print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                    print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                    print('', 42, ''.rjust(width), '', 42, '')
                    print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                    print('', 44, ''.rjust(width), '', 44, '')
                    print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                    print('', 46, ''.center(width), '', 46, '')
                    print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                    width = 92
                    PATTERN = (input(" ".center(width)))

                    # SELECTING FROM VARIOUS PATTERNS......1
                    if PATTERN == '1':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                        l = int(input("       ENTER LENGTH:"))
                        b = int(input("       ENTER BREADTH:"))
                        for i in range(1, l + 1):
                            for j in range(1, b + 1):
                                if i == 1 or i == l or j == 1 or j == b:

                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                        # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                        n = int(input("       ENTER SIDE:"))
                        for i in range(1, n + 1):
                            for j in range(1, n + 1):
                                if i == 1 or i == n or j == 1 or j == n:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()

                        print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                        row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                        col = row
                        for i in range(row):
                            for j in range(col):
                                if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                        i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                        j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                    print('*', end=' ')  # end='' so that print statement should not change the line.

                                else:
                                    print(' ', end=' ')  # to print the space.
                            print()  # to change the line after iteration of inner loop.

                        print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                        n = int(input("       ENTER HEIGHT:"))
                        for row in range(1, n + 1):
                            for col in range(1, 2 * n):
                                if row == n or row + col == n + 1 or col - row == n - 1:
                                    print('*', end=' ')
                                else:
                                    print(' ', end=' ')
                            print()



                    # SELECTING FROM VARIOUS PATTERNS......2
                    elif PATTERN == '2':
                        width = 180
                        print('', 48, ''.rjust(width), '', 48, '')
                        print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                        print('', 50, ''.rjust(width), '', 50, '')

                        # URSA MAJOR HEADING
                        msg = " 51"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MAJOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   51\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 160  # URSA MAJOR PATTERN
                        print('*'.center(width))
                        width = 170
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 200
                        print('*'.center(width))  # /URSA MAJOR PATTERN
                        print()
                        print()

                        # URSA MINOR HEADING
                        width = 180
                        msg = " 52"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- URSA MINOR ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   52\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # URSA MINOR PATTERN
                        print('*'.center(width))
                        print()
                        width = 190
                        print('*'.center(width))
                        print()
                        width = 185
                        print('*'.center(width))
                        for i in range(1, 4):
                            print()
                        width = 188
                        print('*'.center(width))
                        width = 175
                        print('*'.center(width))
                        print()
                        print()
                        width = 193
                        print('*'.center(width))
                        width = 183
                        print('*'.center(width))  # /URSA MINOR PATTERN
                        print()
                        print()

                        # ORION HEADING
                        width = 180
                        msg = " 53"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ORION ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   53\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 200  # ORION PATTERN
                        print('*'.center(width))
                        print()
                        width = 170
                        print('*'.center(width))
                        print()
                        width = 210
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()

                        width = 193
                        print('*'.center(width))
                        width = 188
                        print('*'.center(width))
                        width = 182
                        print('*'.center(width))
                        for i in range(1, 7):
                            print()
                        width = 210
                        print('*'.center(width))
                        width = 168
                        print('*'.center(width))  # /ORION PATTERN
                        print()
                        print()

                        # CASSIOPEIA HEADING
                        width = 180
                        msg = " 54"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- CASSIOPEIA ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   54\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 210  # CASSIOPEIA PATTERN
                        print('*'.center(width))
                        print()
                        print()
                        width = 180
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 140
                        print('*'.center(width))
                        width = 173
                        print('*'.center(width))  # /CASSIOPEIA PATTERN
                        print()
                        print()

                        # ARIES HEADING
                        width = 180
                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "---- ARIES ----".center(width)
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print()
                        width = 180  # ARIES PATTERN
                        print('*'.center(width))
                        print()
                        width = 200
                        print('*'.center(width))
                        width = 207
                        print('*'.center(width))
                        width = 205
                        print('*'.center(width))  # /ARIES PATTERN
                        print()

                # END OF CHOICE= 2
                width = 180
                print()
                msg = " 55"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                msg = "   55\n"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                for i in range(56, 61):
                    print('', i, ''.rjust(width), '', i, '')

                # MORE  ABOVE CODING  OF PLAY WITH NUMBERS..........................................................


            elif A_C == 'no':
                width = 180
                print()
                print('', 35, 'OK BYE'.center(width), '', 35, '')
                print('', 36, 'ENJOY YOUR DAY :)'.center(width), '', 36, '')
                for i in range(37, 51):
                    print('', i, ''.rjust(width), '', i, '')

                    '''WHATTODO FINALLY FINISHED'''



        #.................................................................



    #WHEN THE ANSWER IS WRONG:GIVING ANOTHER CHANCE'''
    else:
        print('', 15, ''.rjust(width), '', 15, '')
        print('', 16, '|OHH SORRY! YOU ARE WRONG|'.center(width), '', 16, '')
        print('', 17, ' DO YOU WANT TO GIVE IT ANOTHER TRY (yes or no)'.center(width), '', 17, '')
        width = 92
        C = (input(" ".center(width)))

        '''IF THE USER AGREES TO TRY AGAIN'''
        if C == 'yes':
            width = 180
            print('', 18, ''.rjust(width), '', 18, '')
            print('', 19, 'TYPE YOUR ANSWER AGAIN:-'.center(width), '', 19, '')
            print('', 20, ''.rjust(width), '', 20, '')
            width = 85
            D = (input(" ".center(width)))
            width = 180

            '''IF 2ND ANSWER IS CORRECT'''
            if D == B:
                print('', "*", ''.rjust(width), '', " *", '')
                print('', "*", 'YOU GOT IT RIGHT...FINALLY!'.center(width), '', " *", '')
                print('', "*", '|YOU ARE SUCCESSFULLY LOGGED IN|'.center(width), '', " *", '')
                print('', "*", ''.rjust(width), '', " *", '')
                print()


                # MAIN TOPIC STARTS FROM HERE I.E. WHAT TO DO WITH NUMBERS

                print('', 21, ''.rjust(width), '', 21, '')
                print('', 22, 'NOW SELECT WHAT DO YOU WANT TO DO WITH NUMBERS'.center(width), '', 22, '')
                print('', 23, 'PLAY WITH NUMBERS(PRESS 1)'.ljust(width), '', 23, '')
                print('', 24, 'OR'.center(width), '', 24, '')
                print('', 25, 'FIND OUT VARIOUS NUMBER SEQUENCE(PRESS 2)'.rjust(width), '', 25, '')
                width = 93
                WHATTODO = (input(" ".center(width)))

                # PLAY WITH NUMBERS LOOP START FROM HERE WITH 2 CHOICES

                # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 1)
                if WHATTODO == '1':
                    width = 180
                    print('', 26, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 26, '')

                    # 1st choice

                    msg = " 27"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   27\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    # 2nd choice

                    msg = " 28"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
                    msg = "   28\n"
                    for char in msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)

                    print('', 29, ''.rjust(width), '', 29, '')

                    width = 92
                    CHOICE = (input(" ".center(width)))

                    # SELECTING FROM VARIOUS CHOICES GIVEN
                    if CHOICE == '1':

                        # ALLEN ASSISTANT

                        width = 180
                        print('', 30, ''.rjust(width), '', 30, '')
                        print('', 31, 'WELCOME TO MAGICA'.center(width), '', 31, '')
                        print('', 32, ''.rjust(width), '', 32, '')
                        print('', 33, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 33, '')
                        print('', 34, ''.rjust(width), '', 34, '')

                        width = 173
                        msg = " 35"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(width)  # A 1ST LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   35\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        msg = " 36"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        print(' ALLEN-', end='')
                        msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   36\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # ALLEN USER TALK:-
                        print()
                        USER = (input("      YOU-"))  # ALLEN USER TALK 1
                        print()
                        # /ALLEN USER TALK:-

                        # WHEN USER SAID YES
                        if USER == 'yes':  # when user said yes to allen

                            msg = " 37"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   37\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN 3 DOTS

                            msg = " 38"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print(' ALLEN-', end='')
                            msg = "......".ljust(width)  # A 4TH LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   38\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)  #

                            msg = " 39"  # ALLEN CONTINUES TO TALK
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   39\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                            msg = " 40"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                                width)  # A 6TH LINE AND STEP 1
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   40\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 41"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(
                                width)  # A 7TH LINE AND STEP 2
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   41\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 42"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                                width)  # A 8TH LINE AND STEP 3
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   42\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 43"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(width)  # A 9TH LINE AND STEP 4
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   43\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                                width)  # A 10TH LINE AND STEP 5
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                                width)  # A 11TH LINE AND PART OF STEP 5
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 46"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                                width)  # A 12TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            msg = "   46\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 47"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                                width)  # A 13TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            msg = "   47\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN USER TALK:-
                            print()
                            USER_ANS = int(input("    YOUR ANS-"))
                            USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                            DIFF = USER_ANS - USER_ANS2
                            AGE = DIFF % 100
                            CHOOSEN_NO = DIFF // 100
                            print()
                            # /ALLEN USER TALK:-

                            msg = " 48"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print(' ALLEN-', end='')
                            msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                                width)  # A 14TH LINE ( SIMPLE TALK)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   48\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)

                            print()
                            print('    ALLEN- ', end='')
                            print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                            print(AGE, "YEARS")

                            print('    ALLEN- ', end='')
                            print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                                  end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                            print(CHOOSEN_NO)
                            print()

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 49, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 49,
                                  '')
                            print()
                            width = 93
                            A_C2 = (input(" ".center(width)))
                            print()
                            if A_C2 == 'yes':
                                width = 180
                                print('', 50, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 50, '')
                                print()
                                print('', 51, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 51, '')
                                width = 95
                                print('', 52, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 52, '')
                                width = 180
                                print('', 53, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 53, '')
                                width = 300
                                print('', 54,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         54'.center(
                                          width))
                                width = 180
                                print('', 55, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 55, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 56, '---EVEN NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 56, '---ODD NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 56, '---PRIME NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 56, '---COMPOSITE NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 56, '---FIBONACCHI NUMBERS---'.center(width), '', 56, '')
                                    print()
                                    print('', 57,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 57, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                '''END OF WHATTODO=2'''

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 58"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   58\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(59, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif A_C2 == 'no':
                                width = 180
                                print()
                                print('', 49, 'OK BYE'.center(width), '', 49, '')
                                print('', 50, 'ENJOY YOUR DAY :)'.center(width), '', 50, '')
                                for i in range(51, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''MAGIC YES FINALLY FINISHED'''

                        # WHEN USER SAID NO
                        elif USER == 'no':  # when user said no to allen

                            msg = " 37"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   37\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 38"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   38\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # OFFERING 2ND CHOICE TO USER.................................
                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                            print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                            print('', 42, ''.rjust(width), '', 42, '')
                            print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                            print('', 44, ''.rjust(width), '', 44, '')
                            print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                            print('', 46, ''.center(width), '', 46, '')
                            print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                            width = 92
                            PATTERN = (input(" ".center(width)))

                            # SELECTING FROM VARIOUS PATTERNS......1
                            if PATTERN == '1':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                                l = int(input("       ENTER LENGTH:"))
                                b = int(input("       ENTER BREADTH:"))
                                for i in range(1, l + 1):
                                    for j in range(1, b + 1):
                                        if i == 1 or i == l or j == 1 or j == b:

                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                                # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                n = int(input("       ENTER SIDE:"))
                                for i in range(1, n + 1):
                                    for j in range(1, n + 1):
                                        if i == 1 or i == n or j == 1 or j == n:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                                row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                col = row
                                for i in range(row):
                                    for j in range(col):
                                        if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                            print('*',
                                                  end=' ')  # end='' so that print statement should not change the line.

                                        else:
                                            print(' ', end=' ')  # to print the space.
                                    print()  # to change the line after iteration of inner loop.

                                print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                                n = int(input("       ENTER HEIGHT:"))
                                for row in range(1, n + 1):
                                    for col in range(1, 2 * n):
                                        if row == n or row + col == n + 1 or col - row == n - 1:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()



                            # SELECTING FROM VARIOUS PATTERNS......2
                            elif PATTERN == '2':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                # URSA MAJOR HEADING
                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MAJOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 160  # URSA MAJOR PATTERN
                                print('*'.center(width))
                                width = 170
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 200
                                print('*'.center(width))  # /URSA MAJOR PATTERN
                                print()
                                print()

                                # URSA MINOR HEADING
                                width = 180
                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MINOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # URSA MINOR PATTERN
                                print('*'.center(width))
                                print()
                                width = 190
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                for i in range(1, 4):
                                    print()
                                width = 188
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                print()
                                width = 193
                                print('*'.center(width))
                                width = 183
                                print('*'.center(width))  # /URSA MINOR PATTERN
                                print()
                                print()

                                # ORION HEADING
                                width = 180
                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ORION ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # ORION PATTERN
                                print('*'.center(width))
                                print()
                                width = 170
                                print('*'.center(width))
                                print()
                                width = 210
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()

                                width = 193
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 182
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()
                                width = 210
                                print('*'.center(width))
                                width = 168
                                print('*'.center(width))  # /ORION PATTERN
                                print()
                                print()

                                # CASSIOPEIA HEADING
                                width = 180
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- CASSIOPEIA ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 210  # CASSIOPEIA PATTERN
                                print('*'.center(width))
                                print()
                                print()
                                width = 180
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 140
                                print('*'.center(width))
                                width = 173
                                print('*'.center(width))  # /CASSIOPEIA PATTERN
                                print()
                                print()

                                # ARIES HEADING
                                width = 180
                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ARIES ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 180  # ARIES PATTERN
                                print('*'.center(width))
                                print()
                                width = 200
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))  # /ARIES PATTERN
                                print()

                            # END OF CHOICE= 1 WHEN USER SAY 'NO'

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 55, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 55,
                                  '')
                            print()
                            width = 93
                            A_C2 = (input(" ".center(width)))
                            print()
                            if A_C2 == 'yes':
                                width = 180
                                print('', 56, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 56, '')
                                print()
                                print('', 57, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 57, '')
                                width = 95
                                print('', 58, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 58, '')
                                width = 180
                                print('', 59, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 59, '')
                                width = 300
                                print('', 60,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         60'.center(
                                          width))
                                width = 180
                                print('', 61, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 61, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 62, '---EVEN NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 62, '---ODD NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 62, '---PRIME NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 62, '---COMPOSITE NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 62, '---FIBONACCHI NUMBERS---'.center(width), '', 62, '')
                                    print()
                                    print('', 63,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 63, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                    '''END OF WHATTODO=2'''

                                    # END OF CHOICE= 2
                                    width = 180
                                    print()
                                    msg = " 64"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   64\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    for i in range(65, 71):
                                        print('', i, ''.rjust(width), '', i, '')

                            elif A_C2 == 'no':
                                width = 180
                                print()
                                print('', 55, 'OK BYE'.center(width), '', 55, '')
                                print('', 56, 'ENJOY YOUR DAY :)'.center(width), '', 56, '')
                                for i in range(57, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''




                    # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                    elif CHOICE == '2':
                        width = 180
                        print('', 30, ''.rjust(width), '', 30, '')
                        print('', 31, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 31, '')
                        print('', 31, 'WELCOME TO PATTERNS'.center(width), '', 31, '')
                        print('', 32, ''.rjust(width), '', 32, '')
                        print('', 33, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 33, '')
                        print('', 34, ''.rjust(width), '', 34, '')
                        print('', 35, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 35, '')
                        print('', 36, ''.center(width), '', 36, '')
                        print('', 37, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 37, '')
                        width = 92
                        PATTERN = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS PATTERNS......1
                        if PATTERN == '1':
                            width = 180
                            print('', 38, ''.rjust(width), '', 38, '')
                            print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                            print('', 40, ''.rjust(width), '', 40, '')

                            print('', 41, '* RECTANGLE'.ljust(width), '', 41, '')  # RECTANGLE IS MADE HERE
                            l = int(input("       ENTER LENGTH:"))
                            b = int(input("       ENTER BREADTH:"))
                            for i in range(1, l + 1):
                                for j in range(1, b + 1):
                                    if i == 1 or i == l or j == 1 or j == b:

                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 42, '* SQUARE'.ljust(width), '', 42, '')  # SQUARE IS MADE HERE
                            # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                            n = int(input("       ENTER SIDE:"))
                            for i in range(1, n + 1):
                                for j in range(1, n + 1):
                                    if i == 1 or i == n or j == 1 or j == n:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            print('', 43, '* CIRCLE'.ljust(width), '', 43, '')  # CIRCLE IS MADE HERE
                            row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                            col = row
                            for i in range(row):
                                for j in range(col):
                                    if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                            i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                            j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                        print('*',
                                              end=' ')  # end='' so that print statement should not change the line.

                                    else:
                                        print(' ', end=' ')  # to print the space.
                                print()  # to change the line after iteration of inner loop.

                            print('', 44, '* TRIANGLE'.ljust(width), '', 44, '')  # TRIANGLE IS MADE HERE
                            n = int(input("       ENTER HEIGHT:"))
                            for row in range(1, n + 1):
                                for col in range(1, 2 * n):
                                    if row == n or row + col == n + 1 or col - row == n - 1:
                                        print('*', end=' ')
                                    else:
                                        print(' ', end=' ')
                                print()

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45,
                                  '')
                            print()
                            width = 93
                            AC = (input(" ".center(width)))
                            print()
                            if AC == 'yes':
                                width = 180
                                print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                                print()
                                print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                                width = 95
                                print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 48, '')
                                width = 180
                                print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                                width = 300
                                print('', 50,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(
                                          width))
                                width = 180
                                print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                    '''END OF WHATTODO=2'''

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(55, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif AC == 'no':
                                width = 180
                                print()
                                print('', 46, 'OK BYE'.center(width), '', 46, '')
                                print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                                for i in range(48, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''


                        # SELECTING FROM VARIOUS PATTERNS......2
                        elif PATTERN == '2':
                            width = 180
                            print('', 38, ''.rjust(width), '', 38, '')
                            print('', 39, 'HERE WE GO:'.center(width), '', 39, '')
                            print('', 40, ''.rjust(width), '', 40, '')

                            # URSA MAJOR HEADING
                            msg = " 41"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MAJOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   41\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 160  # URSA MAJOR PATTERN
                            print('*'.center(width))
                            width = 170
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 200
                            print('*'.center(width))  # /URSA MAJOR PATTERN
                            print()
                            print()

                            # URSA MINOR HEADING
                            width = 180
                            msg = " 42"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- URSA MINOR ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   42\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # URSA MINOR PATTERN
                            print('*'.center(width))
                            print()
                            width = 190
                            print('*'.center(width))
                            print()
                            width = 185
                            print('*'.center(width))
                            for i in range(1, 4):
                                print()
                            width = 188
                            print('*'.center(width))
                            width = 175
                            print('*'.center(width))
                            print()
                            print()
                            width = 193
                            print('*'.center(width))
                            width = 183
                            print('*'.center(width))  # /URSA MINOR PATTERN
                            print()
                            print()

                            # ORION HEADING
                            width = 180
                            msg = " 43"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ORION ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   43\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 200  # ORION PATTERN
                            print('*'.center(width))
                            print()
                            width = 170
                            print('*'.center(width))
                            print()
                            width = 210
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()

                            width = 193
                            print('*'.center(width))
                            width = 188
                            print('*'.center(width))
                            width = 182
                            print('*'.center(width))
                            for i in range(1, 7):
                                print()
                            width = 210
                            print('*'.center(width))
                            width = 168
                            print('*'.center(width))  # /ORION PATTERN
                            print()
                            print()

                            # CASSIOPEIA HEADING
                            width = 180
                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- CASSIOPEIA ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 210  # CASSIOPEIA PATTERN
                            print('*'.center(width))
                            print()
                            print()
                            width = 180
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 140
                            print('*'.center(width))
                            width = 173
                            print('*'.center(width))  # /CASSIOPEIA PATTERN
                            print()
                            print()

                            # ARIES HEADING
                            width = 180
                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "---- ARIES ----".center(width)
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            print()
                            width = 180  # ARIES PATTERN
                            print('*'.center(width))
                            print()
                            width = 200
                            print('*'.center(width))
                            width = 207
                            print('*'.center(width))
                            width = 205
                            print('*'.center(width))  # /ARIES PATTERN
                            print()

                            '''END OF WHATTODO 1'''

                            # ASKING FOR ANOTHER CHOICE TOO FROM THE USER

                            width = 180
                            print()
                            print('', 45, ' DO YOU WANT TO FIND OUT VARIOUS SEQ. TOO?(yes or no)'.center(width), '', 45,
                                  '')
                            print()
                            width = 93
                            AC = (input(" ".center(width)))
                            print()
                            if AC == 'yes':
                                width = 180
                                print('', 46, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 46, '')
                                print()
                                print('', 47, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 47, '')
                                width = 95
                                print('', 48, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                                    '                                '
                                                                                    '                     ', 48, '')
                                width = 180
                                print('', 49, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 49, '')
                                width = 300
                                print('', 50,
                                      'COMPOSITE NUMBERS(PRESS 4)                                         50'.center(
                                          width))
                                width = 180
                                print('', 51, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 51, '')
                                width = 93
                                number_seq = (input(" ".center(width)))

                                # SELECTING NUMBER SEQ. FROM ABOVE

                                # EVEN NUMBER.....
                                if number_seq == '1':
                                    width = 180
                                    print()
                                    print('', 52, '---EVEN NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')

                                # ODD NUMBER.....
                                elif number_seq == '2':
                                    width = 180
                                    print()
                                    print('', 52, '---ODD NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(1, limit + 1):
                                            if i % 2 != 0:
                                                print('', i, end=' ,')


                                # PRIME NUMBERS.....
                                elif number_seq == '3':
                                    width = 180
                                    print()
                                    print('', 52, '---PRIME NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '',
                                          53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        print(''.center(width), '2')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        print('2 ,', end='')
                                        for i in range(1, limit + 1):
                                            if i != 1 and i % 2 != 0:
                                                print('', i, end=' ,')


                                # COMPOSITE NUMBERS.....
                                elif number_seq == '4':
                                    width = 180
                                    print()
                                    print('', 52, '---COMPOSITE NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print(''.center(width), i, end=' ')
                                            print()
                                    elif limit > 50:
                                        for i in range(4, limit + 1):
                                            if i % 2 == 0:
                                                print('', i, end=' ,')


                                # FIBONACCHI NUMBERS.....
                                elif number_seq == '5':
                                    width = 180
                                    print()
                                    print('', 52, '---FIBONACCHI NUMBERS---'.center(width), '', 52, '')
                                    print()
                                    print('', 53,
                                          'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width),
                                          '', 53, '')
                                    width = 93
                                    limit = int(input(" ".center(width)))
                                    print()
                                    if limit <= 25:
                                        a, b = 1, 1
                                        print(''.center(width), a)
                                        print()
                                        print(''.center(width), b)
                                        print()
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print(''.center(width), c, end='\n')
                                            print()
                                    elif limit > 25:
                                        a, b = 1, 1
                                        print(a, ',', end='')
                                        print('', b, ',', end='')
                                        for i in range(limit - 2):
                                            c = a + b
                                            b = a
                                            a = c
                                            print('', c, end=' ,')

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(55, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            elif AC == 'no':
                                width = 180
                                print()
                                print('', 46, 'OK BYE'.center(width), '', 46, '')
                                print('', 47, 'ENJOY YOUR DAY :)'.center(width), '', 47, '')
                                for i in range(48, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                                    '''WHATTODO FINALLY FINISHED'''



                # SELECTING VARIOUS OPTIONS (STARTING WHAT TO DO 2)
                elif WHATTODO == '2':
                    width = 180
                    print('', 26, 'SELECT WHICH TYPE OF NUMBER SEQ. YOU WANT'.center(width), '', 26, '')
                    print()
                    print('', 27, 'EVEN NUMBERS(PRESS 1)'.ljust(width), '', 27, '')
                    width = 95
                    print('', 28, 'ODD NUMBERS(PRESS 2)'.center(width), '                                '
                                                                        '                                '
                                                                        '                     ', 28, '')
                    width = 180
                    print('', 29, 'PRIME NUMBERS(PRESS 3)'.center(width), '', 29, '')
                    width = 300
                    print('', 30, 'COMPOSITE NUMBERS(PRESS 4)                                         30'.center(width))
                    width = 180
                    print('', 31, 'FIBONACCHI NUMBERS(PRESS 5)'.rjust(width), '', 31, '')
                    width = 93
                    number_seq = (input(" ".center(width)))

                    # SELECTING NUMBER SEQ. FROM ABOVE

                    # EVEN NUMBER.....
                    if number_seq == '1':
                        width = 180
                        print()
                        print('', 32, '---EVEN NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE EVEN SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(1, limit + 1):
                                if i % 2 == 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(1, limit + 1):
                                if i % 2 == 0:
                                    print('', i, end=' ,')

                    # ODD NUMBER.....
                    elif number_seq == '2':
                        width = 180
                        print()
                        print('', 32, '---ODD NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE ODD SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(1, limit + 1):
                                if i % 2 != 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(1, limit + 1):
                                if i % 2 != 0:
                                    print('', i, end=' ,')


                    # PRIME NUMBERS.....
                    elif number_seq == '3':
                        width = 180
                        print()
                        print('', 32, '---PRIME NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE PRIME SEQ.'.center(width), '', 33,
                              '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            print(''.center(width), '2')
                            for i in range(1, limit + 1):
                                if i != 1 and i % 2 != 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            print('2 ,', end='')
                            for i in range(1, limit + 1):
                                if i != 1 and i % 2 != 0:
                                    print('', i, end=' ,')


                    # COMPOSITE NUMBERS.....
                    elif number_seq == '4':
                        width = 180
                        print()
                        print('', 32, '---COMPOSITE NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE COMPOSITE SEQ.'.center(width), '',
                              33, '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 50:
                            for i in range(4, limit + 1):
                                if i % 2 == 0:
                                    print(''.center(width), i, end=' ')
                                print()
                        elif limit > 50:
                            for i in range(4, limit + 1):
                                if i % 2 == 0:
                                    print('', i, end=' ,')


                    # FIBONACCHI NUMBERS.....
                    elif number_seq == '5':
                        width = 180
                        print()
                        print('', 32, '---FIBONACCHI NUMBERS---'.center(width), '', 32, '')
                        print()
                        print('', 33, 'ENTER THE LAST NUMBER UPTO WHICH YOU WANT THE FIBONACCHI SEQ.'.center(width), '',
                              33, '')
                        width = 93
                        limit = int(input(" ".center(width)))
                        print()
                        if limit <= 25:
                            a, b = 1, 1
                            print(''.center(width), a)
                            print()
                            print(''.center(width), b)
                            print()
                            for i in range(limit - 2):
                                c = a + b
                                b = a
                                a = c
                                print(''.center(width), c, end='\n')
                                print()
                        elif limit > 25:
                            a, b = 1, 1
                            print(a, ',', end='')
                            print('', b, ',', end='')
                            for i in range(limit - 2):
                                c = a + b
                                b = a
                                a = c
                                print('', c, end=' ,')  # END OF WHAT TO DO 2

                    # ASKING FOR ANOTHER CHOICE TOO FROM THE USER
                    width = 180
                    print()
                    print('', 34, ' DO YOU WANT TO PLAY WITH NUMBERS TOO?(yes or no)'.center(width), '', 34, '')
                    print()
                    width = 93
                    A_C = (input(" ".center(width)))
                    print()
                    if A_C == 'yes':
                        width = 180
                        print('', 35, 'OK SO SELECT YOUR FAV. CHOICE'.center(width), '', 35, '')

                        # 1st choice

                        msg = " 36"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "WANNA DO MAGIC TRICK(PRESS 1)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   36\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        # 2nd choice

                        msg = " 37"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "WANNA MAKE PATTERNS(PRESS 2)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   37\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)

                        print('', 38, ''.rjust(width), '', 38, '')

                        width = 92
                        CHOICE = (input(" ".center(width)))

                        # SELECTING FROM VARIOUS CHOICES GIVEN
                        if CHOICE == '1':

                            # ALLEN ASSISTANT

                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, 'WELCOME TO MAGICA'.center(width), '', 40, '')
                            print('', 41, ''.rjust(width), '', 41, '')
                            print('', 42, 'MEET "ALLEN" HE IS YOUR ASSISTANT '.center(width), '', 42, '')
                            print('', 43, ''.rjust(width), '', 43, '')

                            width = 173
                            msg = " 44"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "HELLO I AM ALLEN...I AM GOING TO DO A MAGIC TRICK WITH YOU.".ljust(
                                width)  # A 1ST LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   44\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            msg = " 45"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            print(' ALLEN-', end='')
                            msg = "ARE YOU READY?(yes or no)".ljust(width)  # A 2ND LINE
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)
                            msg = "   45\n"
                            for char in msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.01)

                            # ALLEN USER TALK:-
                            print()
                            USER = (input("      YOU-"))  # ALLEN USER TALK 1
                            print()
                            # /ALLEN USER TALK:-

                            # WHEN USER SAID YES
                            if USER == 'yes':  # when user said yes to allen

                                msg = " 46"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "OK FINE! I WILL MAKE YOU BELEIVE IN MAGIC.".ljust(width)  # A 3RD LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   46\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # ALLEN 3 DOTS

                                msg = " 47"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(' ALLEN-', end='')
                                msg = "......".ljust(width)  # A 4TH LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   47\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)  #

                                msg = " 48"  # ALLEN CONTINUES TO TALK
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "UMM,S0... DO AS I SAY.".ljust(width)  # A 5TH LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   48\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # NOW HERE MAGIC TRICK BEGINS......MORE CODING..........
                                msg = " 49"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " THINK OF A NUMBER BETWEEN 1-9.....SHH DON'T TELL ANYONE.".ljust(
                                    width)  # A 6TH LINE AND STEP 1
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   49\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 50"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " NOW MULTIPLY THE NUMBER BY '2' AND ADD '5' TO IT.".ljust(
                                    width)  # A 7TH LINE AND STEP 2
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   50\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " IF YOU HAVE DONE THIS MUCH....MULTIPLY THE PREVIOUS ANSWER BY '50'.".ljust(
                                    width)  # A 8TH LINE AND STEP 3
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " OK YOU ARE DOING GREAT....JUST ONE MORE STEP.".ljust(
                                    width)  # A 9TH LINE AND STEP 4
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " IF YOU HAVE CELEBRATED YOUR BIRTHDAY THIS YEAR ADD '1770'. ".ljust(
                                    width)  # A 10TH LINE AND STEP 5
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " BUT IF YOUR BIRTHDAY IS YET TO ARRIVE THIS YEAR.... ADD '1769' (TO YOUR CURRENT ANSWER). ".ljust(
                                    width)  # A 11TH LINE AND PART OF STEP 5
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " WELL...I KNOW ITS A LENTHY CALCULATION...BUT YEAH TAKE YOUR TIME.".ljust(
                                    width)  # A 12TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 56"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = " WHEN YOU ARE DONE....TYPE THE ANSWER YOU OBTAINED AND THEN YOUR YEAR OF BIRTH.".ljust(
                                    width)  # A 13TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                msg = "   56\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # ALLEN USER TALK:-
                                print()
                                USER_ANS = int(input("    YOUR ANS-"))
                                USER_ANS2 = int(input("    YOUR YOB-"))  # ALLEN USER TALK 2
                                DIFF = USER_ANS - USER_ANS2
                                AGE = DIFF % 100
                                CHOOSEN_NO = DIFF // 100
                                print()
                                # /ALLEN USER TALK:-

                                msg = " 57"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(' ALLEN-', end='')
                                msg = " ROSES ARE RED.....VIOLETS ARE BLUE.....I WILL TELL YOU YOUR AGE.....AND THE NUMBER YOU HAVE CHOOSE :)".ljust(
                                    width)  # A 14TH LINE ( SIMPLE TALK)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   57\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print()
                                print('    ALLEN- ', end='')
                                print("SO YOUR AGE IS: ", end='')  # A 15TH LINE (CLIMAX ..TELLING THE AGE)
                                print(AGE, "YEARS")

                                print('    ALLEN- ', end='')
                                print("AND THE NUMBER YOU HAVE CHOOSEN IS: ",
                                      end='')  # A 16TH LINE (CLIMAX ..TELLING THE NUMBER)
                                print(CHOOSEN_NO)
                                print()

                                # END OF CHOICE= 1 WHEN USER SAY 'YES'
                                width = 180
                                print()
                                msg = " 58"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   58\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(59, 61):
                                    print('', i, ''.rjust(width), '', i, '')

                            # WHEN USER SAID NO
                            elif USER == 'no':  # when user said no to allen

                                msg = " 46"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "OK FINE YOU CAN TRY SOMETHING ELSE".ljust(width)  # A NO 1ST LINE
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   46\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                msg = " 47"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                print(' ALLEN-', end='')
                                msg = "BBYE".ljust(width)  # A NO 2ND LINE (LAST LINE)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   47\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                # OFFERING 2ND CHOICE TO USER.................................
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 49, '')
                                print('', 50, 'WELCOME TO PATTERNS'.center(width), '', 50, '')
                                print('', 51, ''.rjust(width), '', 51, '')
                                print('', 52, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 52, '')
                                print('', 53, ''.rjust(width), '', 53, '')
                                print('', 54, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 54, '')
                                print('', 55, ''.center(width), '', 55, '')
                                print('', 56, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 56, '')
                                width = 92
                                PATTERN = (input(" ".center(width)))

                                # SELECTING FROM VARIOUS PATTERNS......1
                                if PATTERN == '1':
                                    width = 180
                                    print('', 57, ''.rjust(width), '', 57, '')
                                    print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                                    print('', 59, ''.rjust(width), '', 59, '')

                                    print('', 60, '* RECTANGLE'.ljust(width), '', 60, '')  # RECTANGLE IS MADE HERE
                                    l = int(input("       ENTER LENGTH:"))
                                    b = int(input("       ENTER BREADTH:"))
                                    for i in range(1, l + 1):
                                        for j in range(1, b + 1):
                                            if i == 1 or i == l or j == 1 or j == b:

                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()

                                    print('', 61, '* SQUARE'.ljust(width), '', 61, '')  # SQUARE IS MADE HERE
                                    # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                    n = int(input("       ENTER SIDE:"))
                                    for i in range(1, n + 1):
                                        for j in range(1, n + 1):
                                            if i == 1 or i == n or j == 1 or j == n:
                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()

                                    print('', 62, '* CIRCLE'.ljust(width), '', 62, '')  # CIRCLE IS MADE HERE
                                    row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                    col = row
                                    for i in range(row):
                                        for j in range(col):
                                            if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                    i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                    j == 1 or j == col - 2) or i == row - 2 and (
                                                    j == 1 or j == col - 2):
                                                print('*',
                                                      end=' ')  # end='' so that print statement should not change the line.

                                            else:
                                                print(' ', end=' ')  # to print the space.
                                        print()  # to change the line after iteration of inner loop.

                                    print('', 63, '* TRIANGLE'.ljust(width), '', 63, '')  # TRIANGLE IS MADE HERE
                                    n = int(input("       ENTER HEIGHT:"))
                                    for row in range(1, n + 1):
                                        for col in range(1, 2 * n):
                                            if row == n or row + col == n + 1 or col - row == n - 1:
                                                print('*', end=' ')
                                            else:
                                                print(' ', end=' ')
                                        print()



                                # SELECTING FROM VARIOUS PATTERNS......2
                                elif PATTERN == '2':
                                    width = 180
                                    print('', 57, ''.rjust(width), '', 57, '')
                                    print('', 58, 'HERE WE GO:'.center(width), '', 58, '')
                                    print('', 59, ''.rjust(width), '', 59, '')

                                    # URSA MAJOR HEADING
                                    msg = " 60"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- URSA MAJOR ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   60\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 160  # URSA MAJOR PATTERN
                                    print('*'.center(width))
                                    width = 170
                                    print('*'.center(width))
                                    width = 175
                                    print('*'.center(width))
                                    print()
                                    width = 185
                                    print('*'.center(width))
                                    width = 205
                                    print('*'.center(width))
                                    width = 188
                                    print('*'.center(width))
                                    width = 200
                                    print('*'.center(width))  # /URSA MAJOR PATTERN
                                    print()
                                    print()

                                    # URSA MINOR HEADING
                                    width = 180
                                    msg = " 61"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- URSA MINOR ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   61\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 200  # URSA MINOR PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 190
                                    print('*'.center(width))
                                    print()
                                    width = 185
                                    print('*'.center(width))
                                    for i in range(1, 4):
                                        print()
                                    width = 188
                                    print('*'.center(width))
                                    width = 175
                                    print('*'.center(width))
                                    print()
                                    print()
                                    width = 193
                                    print('*'.center(width))
                                    width = 183
                                    print('*'.center(width))  # /URSA MINOR PATTERN
                                    print()
                                    print()

                                    # ORION HEADING
                                    width = 180
                                    msg = " 62"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- ORION ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   62\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 200  # ORION PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 170
                                    print('*'.center(width))
                                    print()
                                    width = 210
                                    print('*'.center(width))
                                    for i in range(1, 7):
                                        print()

                                    width = 193
                                    print('*'.center(width))
                                    width = 188
                                    print('*'.center(width))
                                    width = 182
                                    print('*'.center(width))
                                    for i in range(1, 7):
                                        print()
                                    width = 210
                                    print('*'.center(width))
                                    width = 168
                                    print('*'.center(width))  # /ORION PATTERN
                                    print()
                                    print()

                                    # CASSIOPEIA HEADING
                                    width = 180
                                    msg = " 63"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- CASSIOPEIA ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   63\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 210  # CASSIOPEIA PATTERN
                                    print('*'.center(width))
                                    print()
                                    print()
                                    width = 180
                                    print('*'.center(width))
                                    width = 207
                                    print('*'.center(width))
                                    width = 140
                                    print('*'.center(width))
                                    width = 173
                                    print('*'.center(width))  # /CASSIOPEIA PATTERN
                                    print()
                                    print()

                                    # ARIES HEADING
                                    width = 180
                                    msg = " 64"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "---- ARIES ----".center(width)
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)
                                    msg = "   64\n"
                                    for char in msg:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(0.01)

                                    print()
                                    width = 180  # ARIES PATTERN
                                    print('*'.center(width))
                                    print()
                                    width = 200
                                    print('*'.center(width))
                                    width = 207
                                    print('*'.center(width))
                                    width = 205
                                    print('*'.center(width))  # /ARIES PATTERN
                                    print()

                                # END OF CHOICE= 2
                                width = 180
                                print()
                                msg = " 64"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   64\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                for i in range(65, 71):
                                    print('', i, ''.rjust(width), '', i, '')

                            # END OF CHOICE= 1 WHEN USER SAY 'NO'





                        # SELECTING FROM VARIOUS CHOICES GIVEN ( OFFICIALLY STARTING CHOICE 2)
                        elif CHOICE == '2':
                            width = 180
                            print('', 39, ''.rjust(width), '', 39, '')
                            print('', 40, '---SO HERE IS ANOTHER OPTION---'.center(width), '', 40, '')
                            print('', 41, 'WELCOME TO PATTERNS'.center(width), '', 41, '')
                            print('', 42, ''.rjust(width), '', 42, '')
                            print('', 43, 'WHAT TYPE OF PATTERNS DO YOU WANT '.center(width), '', 43, '')
                            print('', 44, ''.rjust(width), '', 44, '')
                            print('', 45, 'VARIOUS SIMPLE PATTERNS OF FIG.(press 1)'.ljust(width), '', 45, '')
                            print('', 46, ''.center(width), '', 46, '')
                            print('', 47, 'CONSTELLATION OF STARS(press 2)'.rjust(width), '', 47, '')
                            width = 92
                            PATTERN = (input(" ".center(width)))

                            # SELECTING FROM VARIOUS PATTERNS......1
                            if PATTERN == '1':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                print('', 51, '* RECTANGLE'.ljust(width), '', 51, '')  # RECTANGLE IS MADE HERE
                                l = int(input("       ENTER LENGTH:"))
                                b = int(input("       ENTER BREADTH:"))
                                for i in range(1, l + 1):
                                    for j in range(1, b + 1):
                                        if i == 1 or i == l or j == 1 or j == b:

                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 52, '* SQUARE'.ljust(width), '', 52, '')  # SQUARE IS MADE HERE
                                # NOTE- NUMBER BORDER PATTERN HAS TO BE CORRECTED
                                n = int(input("       ENTER SIDE:"))
                                for i in range(1, n + 1):
                                    for j in range(1, n + 1):
                                        if i == 1 or i == n or j == 1 or j == n:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()

                                print('', 53, '* CIRCLE'.ljust(width), '', 53, '')  # CIRCLE IS MADE HERE
                                row = int(input("       ENTER DIAMETER(for diamond press 5):"))
                                col = row
                                for i in range(row):
                                    for j in range(col):
                                        if (j == 0 or j == col - 1) and i in range(2, row - 2) or (
                                                i == 0 or i == row - 1) and j in range(2, col - 2) or i == 1 and (
                                                j == 1 or j == col - 2) or i == row - 2 and (j == 1 or j == col - 2):
                                            print('*',
                                                  end=' ')  # end='' so that print statement should not change the line.

                                        else:
                                            print(' ', end=' ')  # to print the space.
                                    print()  # to change the line after iteration of inner loop.

                                print('', 54, '* TRIANGLE'.ljust(width), '', 54, '')  # TRIANGLE IS MADE HERE
                                n = int(input("       ENTER HEIGHT:"))
                                for row in range(1, n + 1):
                                    for col in range(1, 2 * n):
                                        if row == n or row + col == n + 1 or col - row == n - 1:
                                            print('*', end=' ')
                                        else:
                                            print(' ', end=' ')
                                    print()



                            # SELECTING FROM VARIOUS PATTERNS......2
                            elif PATTERN == '2':
                                width = 180
                                print('', 48, ''.rjust(width), '', 48, '')
                                print('', 49, 'HERE WE GO:'.center(width), '', 49, '')
                                print('', 50, ''.rjust(width), '', 50, '')

                                # URSA MAJOR HEADING
                                msg = " 51"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MAJOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   51\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 160  # URSA MAJOR PATTERN
                                print('*'.center(width))
                                width = 170
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 200
                                print('*'.center(width))  # /URSA MAJOR PATTERN
                                print()
                                print()

                                # URSA MINOR HEADING
                                width = 180
                                msg = " 52"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- URSA MINOR ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   52\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # URSA MINOR PATTERN
                                print('*'.center(width))
                                print()
                                width = 190
                                print('*'.center(width))
                                print()
                                width = 185
                                print('*'.center(width))
                                for i in range(1, 4):
                                    print()
                                width = 188
                                print('*'.center(width))
                                width = 175
                                print('*'.center(width))
                                print()
                                print()
                                width = 193
                                print('*'.center(width))
                                width = 183
                                print('*'.center(width))  # /URSA MINOR PATTERN
                                print()
                                print()

                                # ORION HEADING
                                width = 180
                                msg = " 53"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ORION ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   53\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 200  # ORION PATTERN
                                print('*'.center(width))
                                print()
                                width = 170
                                print('*'.center(width))
                                print()
                                width = 210
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()

                                width = 193
                                print('*'.center(width))
                                width = 188
                                print('*'.center(width))
                                width = 182
                                print('*'.center(width))
                                for i in range(1, 7):
                                    print()
                                width = 210
                                print('*'.center(width))
                                width = 168
                                print('*'.center(width))  # /ORION PATTERN
                                print()
                                print()

                                # CASSIOPEIA HEADING
                                width = 180
                                msg = " 54"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- CASSIOPEIA ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   54\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 210  # CASSIOPEIA PATTERN
                                print('*'.center(width))
                                print()
                                print()
                                width = 180
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 140
                                print('*'.center(width))
                                width = 173
                                print('*'.center(width))  # /CASSIOPEIA PATTERN
                                print()
                                print()

                                # ARIES HEADING
                                width = 180
                                msg = " 55"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "---- ARIES ----".center(width)
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)
                                msg = "   55\n"
                                for char in msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.01)

                                print()
                                width = 180  # ARIES PATTERN
                                print('*'.center(width))
                                print()
                                width = 200
                                print('*'.center(width))
                                width = 207
                                print('*'.center(width))
                                width = 205
                                print('*'.center(width))  # /ARIES PATTERN
                                print()

                        # END OF CHOICE= 2
                        width = 180
                        print()
                        msg = " 55"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "THANK YOU FOR COMING :)".center(width)  # IMPORTANT***
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        msg = "   55\n"
                        for char in msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.01)
                        for i in range(56, 61):
                            print('', i, ''.rjust(width), '', i, '')

                        # MORE  ABOVE CODING  OF PLAY WITH NUMBERS..........................................................


                    elif A_C == 'no':
                        width = 180
                        print()
                        print('', 35, 'OK BYE'.center(width), '', 35, '')
                        print('', 36, 'ENJOY YOUR DAY :)'.center(width), '', 36, '')
                        for i in range(37, 51):
                            print('', i, ''.rjust(width), '', i, '')

                            '''WHATTODO FINALLY FINISHED'''





                #................................................................



            #IF 2ND ANSWER IF WRONG'''
            else:
                print('', 20, ''.rjust(width), '', 20, '')
                print('', 21, '|OHH SORRY! YOU ARE AGAIN WRONG|'.center(width), '', 21, '')
                print('', 22, 'OKK BYE :)'.center(width), '', 22, '')
                for i in range(23, 31):
                    print('', i, ''.rjust(width), '', i, '')

        #IF THE USER DENIES'''
        elif C == 'no':
            width = 180
            print('', 18, 'OKK BYE :)'.center(width), '', 18, '')
            for i in range(19, 31):
                print('', i, ''.rjust(width), '', i, '')




        ####/4 Q/A'''


# ENDING LINES
a = 'X-'
for i in range(1, 33):
    print('', a, end='')
b = '-X'
for i in range(33, 63):
    print('', b, end='')
# /ENDING LINES
