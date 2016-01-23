# The constants describing the multiplicative factor for finding a word in
# a particular direction.  These should be used in function get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4


def get_current_player(player_one_turn):
    """ (bool) -> str

    Return 'Player One' iff player_one_turn is True; otherwise, return 'Player Two'.

    >>> get_current_player(True)
    'Player One'
    >>> get_current_player(False)
    'Player Two'
    """
    
    if player_one_turn == True: 
        return 'Player One' 
    
    else:
        return 'Player Two'

    
    
# Define the other functions from the handout here

def get_winner(player_one_score, player_two_score):
    """(int, int) -> str

    Return 'Player One wins!' iff player_one_score is greater than player_two_score. Return 'Player Two wins!' iff player_two_score is 
    greater than 'player_one_score'. If the game is tied return  'Tie game!'.

    >>> get_winner(35, 20)
    'Player One wins!'
    >>> get_winner(10, 40)
    'Player Two wins!'
    >>> get_winner(29, 29)
    'Tie game!'
    """
    
    if player_one_score > player_two_score:
        return 'Player One wins!'
    
    
    elif player_two_score > player_one_score:
        return 'Player Two wins!'
    
    else: 
        return 'Tie game!'
    

def get_factor(direction):
    """(str) -> int
    Precondition: direction must be 'forward', 'down', 'backward' or up'. 

    Return corresponding factor to direction given.

    >>> get_factor('forward')
    1
    >>> get_factor('down')
    2
    >>> get_factor('backward')
    3
    >>> get_factor('up')
    4
    """

    if direction == 'forward':
        return FORWARD_FACTOR
    
    elif direction == 'down':
        return DOWN_FACTOR

    elif direction == 'backward':
        return BACKWARD_FACTOR

    elif direction == 'up':
        return UP_FACTOR


def get_points(direction, num_words_remaining):
    """(str, int) -> int
    
    Precondition: direction must be 'forward', 'down', 'backward' or up' and num_words_remaining >= 1. 

    With num_words_remaining in consideration, return the player's score if the word is in this direction.

    >>> get_points('backward', 4)
    8
    >>> get_points('down', 15)
    16
    >>> get_points('up', 23)
    42
    >>>get_points('forward', 4)
    108
    """ 
    if num_words_remaining >= 5:
        return  5 * get_factor(direction)
    
    elif num_words_remaining > 1 and num_words_remaining <= 4:  
        return (10 - num_words_remaining) * get_factor(direction)    
    
    #bonus 25 points for finding the last word
    
    elif num_words_remaining == 1: 
        return (10 - num_words_remaining) * get_factor(direction) + 25 
 
    
    
def calculate_score(puzzle, direction, guessed_word, row_or_column,
                    num_words_remaining):
    
    """ (str, str, str, int, int) -> int
    
    Precondition: direction must be 'forward', 'down', 'backward' or 'up', num_words_remaining >= 1 and row_or_column >= 0 and row_or_column <= 9. 


    Return the player's score if the guessed_word is in this direction and row_or_colum in the puzzle and consider the num_words_remaining. 

    >>> calculate_score('abcd\nefgh\nijkl\n', 'up', 'dan', 4, 8)
    10
    
    >>> calculate_score('abcd\nefgh\nijkl\n', 'forward', 'jen', 3, 15)
    8
    """
    zero = 0 
    
    if direction == 'up' or direction == 'down': 
        x = get_column(puzzle, row_or_column) 
        
    elif direction == 'forward'or direction == 'backward': 
        x = get_row(puzzle, row_or_column) 
        
    if direction == 'up' or direction == 'backward': 
        x = reverse(x)
        
    if contains(x, guessed_word):
        return get_points(direction, num_words_remaining)
    
    #if the guessed_word is not found in this direction or row_or_column then return 0 
    
    else:  
        return zero
    

# Helper functions.  Do not modify these, although you are welcome to call
# them.

def get_row(puzzle, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle

    Return row row_num of puzzle.

    >>> get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """

    rows = puzzle.strip().split('\n')
    return rows[row_num]


def get_column(puzzle, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle

    Return column col_num of puzzle.
    >>> get_column('abcde\nefghi\nijklm\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def reverse(s):
    """ (str) -> str

    Return a reversed copy of s.

    >>> reverse('abc')
    'cba'
    """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed

    return s_reversed


def contains(s1, s2):
    """ (str, str) -> bool

    Return whether s2 appears anywhere in s1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return s2 in s1

'''This module should be used to test the parameter and return types of your
functions. Before submitting your assignment, run this type-checker on your
puzzle_functions.py. If errors occur when you run this module, fix them
before you submit your assignment.  

When this module runs, if nothing is displayed and no errors occur, then the
type checks passed. This means that the function parameters and return types
match the assignment specification, but it does not mean that your code works
correctly in all situations. Be sure to test your code before submitting.'''

import puzzle_functions as pf

# Get the initial values of the constants
constants_before = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                    pf.UP_FACTOR]
# Type check pf.get_current_player
result = pf.get_current_player(True)
assert isinstance(result, str), \
       '''pf.get_current_player should return a str, but returned {0}
       .'''.format(type(result))

# Type check pf.get_winner
result = pf.get_winner(17,32)
assert isinstance(result, str), \
       '''pf.get_winner should return a str, but returned {0}.''' \
       .format(type(result))

# Type check pf.get_factor
result = pf.get_factor('forward')
assert isinstance(result, int), \
       '''pf.get_factor should return an int, but returned {0}.''' \
       .format(type(result))


# Type check pf.get_points
result = pf.get_points('up', 7)
assert isinstance(result, int), \
       '''pf.get_points should return an int, but returned {0}.''' \
       .format(type(result))


# Type check pf.calculate_score
result = pf.calculate_score('abcd\nefgh\nijkl\n', 'forward', 'bcd', 2, 4)
assert isinstance(result, int), \
       '''pf.calculate_score should return an int, but returned {0}.''' \
       .format(type(result))

# Get the final values of the constants
constants_after = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                    pf.UP_FACTOR]
# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of a constant(s).
Edit your code so that the values of constants are unchanged by your functions.'''