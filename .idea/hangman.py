import random

hangman = (
    """
    ------
    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |   -+-
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0       
    |  *-+-
    |    
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |  *-+-*
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |  *-+-*
    |    |
    |    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |  *-+-*
    |    |
    |    |
    |   / /
    |
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |  *-+-*
    |    |
    |    |
    |   / /
    |     _| 
    ----------
    """,
    """
    ------
    |    |
    |    |
    |    0
    |  *-+-*
    |    |
    |    |
    |   / /
    |  |_ _|
    ----------
    """
)

maxWrongTries = len(hangman) - 1

wordsToGuess = ('PYTHON', 'PROGRAMMING', 'CODING', 'DEVELOPING', 'MAKING', 'BUILDING', 'CONSTRUCTING', 'LANGUAGE',
                'PRINT', 'INPUT', 'STRING', 'INTEGER', 'FLOAT', 'LEN', 'MUTABLE', 'IMMUTABLE', 'EVALUATE', 'ENUMERATE',
                'RANGE', 'FOR', 'WHILE', 'IF', 'ELIF', 'ELSE', 'CLASS', 'DEFINE', 'LIST', 'TUPLE', 'DICTIONARY', 'SET',
                'VARIABLE', 'IMPORT', 'OS', 'COLORAMA', 'TURTLE', 'PYGAME', 'PPRINT', 'RANDOM', 'TIME', 'PYTZ', 'STOP',
                'DATETIME', 'LAMBDA', 'DATABASE', 'EXPRESSION', 'EQUATION', 'TKINTER', 'GLOBAL', 'GENERATORS', 'AND',
                'OR', 'IN', 'TRUE', 'FALSE', 'RETURN', 'NONE', 'DELETE', 'DISCARD', 'COMPREHENSIONS', 'REMOVE', 'TRY',
                'DEL', 'INSERT', 'PLACE', 'POP', 'MAINLOOP', 'KEY', 'VALUE', 'ITEM', 'SEP', 'END', 'FLUSH', 'FILE',
                'KWARG', 'FUNCTION', 'SLEEP', 'QUIT', 'EXIT', 'CONTINUE', 'BREAK', 'SPLIT', 'JOIN', 'GEOMETRY', 'GRID',
                'PACK', 'TITLE', 'LABEL', 'FRAME', 'UPDATE', 'INTERSECT', 'TIMEZONE', 'NAIVE', 'AWARE', 'LOCAL', 'UTC',
                'SHELVE', 'WITH', 'OPEN', 'CLOSE', 'DESTROY', 'PARAMETER', 'ARGUMENT', 'APPEND', 'AUGMENTED', 'THIS',
                'ASSIGNMENT', 'PICKLE', 'ERROR', 'SYNTAX', 'COMMENT', 'HTML', 'FROM', 'BUTTON', 'LABELFRAME', 'FG',
                'BG', 'COMMAND', 'RELIEF', 'SIDE', 'STICKY', 'WIDGET', 'PADX', 'PADY', 'WIDTH', 'HEIGHT', 'ROWSPAN',
                'COLUMNSPAN', 'BRACKET', 'IPADX', 'IPADY', 'CHOICE', 'SIZE', 'MINIMUM', 'MAXIMUM', 'SUM', 'DESIGNING',
                'HELP', 'GET', 'STRINGVAR', 'SELF', 'CONJUGATE', 'REAL', 'IMAG', 'STR', 'INT', 'NUM', 'DENOMINATOR',
                'NUMERATOR', 'ISINSTANCE', 'USING', 'AS', 'MAIN', 'PAR', 'EQUAL', 'DICT', 'DIR', 'EXEC', 'FILTER',
                'ZIP', 'VARS', 'ITER', 'DIVMOD', 'OCT', 'NEXT', 'MIN', 'MAX', 'BIN', 'BOOL', 'BREAKPOINT', 'COMPILE',
                'ANY', 'COMPLEX', 'CALLABLE', 'ASCII', 'BYTES', 'BYTEARRAY', 'ITERATE', 'CONCATENATE', 'REVERSE',
                'REVERSED', 'CLASSMETHOD', 'CHR', 'ALL', 'ABS', 'OBJECT', 'STATICETHOD', 'SUPER', 'TYPE', 'ID', 'HEX',
                'HASH', 'REPR', 'POW', 'ORD', 'ISSUBCLASS', 'ROUND', 'SORT', 'SORTED', 'MEMORYVIEW', 'SETATTR', 'SLICE',
                'NEXT', 'IMPORTLIB', 'GETATTR', 'PACKAGE', 'DELATTR', 'HASATTR', 'FILL', 'FORWARD', 'RIGHT', 'LEFT',
                'CIRCLE', 'GOTO', 'SETPOS', 'SETPOSITION', 'FSTRING', 'FORMAT', 'PROPERTY', 'SETATTR', 'MATH', 'MODULE',
                'IS', 'CODE', 'PROGRAM', 'DEVELOP', 'BUILD', 'CONSTRUCT', 'MAKE', 'DESIGN', 'MASTER', 'INDEXRANGE',
                'SLICERANGE', 'KEYERROR', 'ARG', 'AST', 'IMPORTERROR', 'VALUEERROR', 'TYPEERROR', 'SYSTEMEXIT', 'DIS')
# There are millions of other words in python, but I only did it till line 150

word = random.choice(wordsToGuess)

soFar = '-' * len(word)

wrongTries = 0

usedLetters = []

print("Welcome to the game of hangman")
print("I will think of a random word, share how many letters it consists and keep track of your guesses")
print("You are only allowed maximum 9 wrong guesses, otherwise you lost.")
print("Right now, you have 9 guesses left to loose and complete the game.")
print("Best of Luck!!!")

while wrongTries < maxWrongTries and soFar != word:
    print(hangman[wrongTries])
    print("You have so far guessed the following letters:\t", usedLetters)
    print("So far, the word is:\t", soFar)

    guessedLetter = input("Please enter your guess: ").upper()

    if guessedLetter.upper() in usedLetters:
        print("You've already guessed that letter, which is", guessedLetter)
        guessedLetter = input("Please enter your guess: ").upper()

    elif guessedLetter.upper() in word:
        print("Well Done!", guessedLetter, " is in my word!")
        newSoFar = ""

        for x in range(len(word)):
            if guessedLetter.upper() == word[x]:
                newSoFar += guessedLetter

            else:
                newSoFar += soFar[x]
        soFar = newSoFar
        print("You still have", maxWrongTries - wrongTries, "wrong guesses left.")

    elif guessedLetter.upper() not in word:
        print("Sorry", guessedLetter, " isn't in the word. Unlucky though!")
        wrongTries += 1
        print("You have", maxWrongTries - wrongTries, "wrong guesses left!")

    if guessedLetter.upper() not in usedLetters:
        usedLetters.append(guessedLetter)

if wrongTries == maxWrongTries:
    print(hangman[wrongTries])
    print("You have not guessed my word and you have had 9 wrong guesses!\n"
          "this means you've been hanged to death!")
    print("My word was", word)
    end = input("Press enter to quit: ")

    if end:
        print("Thank you for playing HANGMAN with me")

elif newSoFar == word:
    print("Amazing! You guessed my word and didn't reach", maxWrongTries, "wrong tries!")
    print("My word was", word)

    end = input("Press enter to quit: ")

    if end == "":
        print("Thank you for playing HANGMAN with me!")


