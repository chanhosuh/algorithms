'''
Created on Jul 4, 2017

@author: suh
'''

import copy

# our alphabet consists of all printable ascii characters
from string import printable, ascii_lowercase

RADIX = ascii_lowercase


def make_shift_table(pattern):
    '''
    The Boyer--Moore algorithm works by starting to match
    the pattern from right to left ("backwards") and using 
    heuristic rules to skip characters in the input stream, 
    e.g. if there is a mismatch and the mismatch character is 
    not in the pattern, shift along the input stream by the 
    length of the pattern.

    The shift table gives, for each pattern index, and for 
    each character in the radix, the amount we shift along the
    input text.
    '''

    shift_dict = {}
    # We start by listing, for each character in the radix, 
    # the index in the pattern of the rightmost occurence of the 
    # character.  An index of -1 means the character doesn't occur.
    for char in RADIX:
        # initialize default shift to -1
        # this will simplify a later calculation
        shift_dict[char] = -1

    for i, p in enumerate(pattern):
        # store rightmost index of char in pattern
        shift_dict[p] = i

    # Now we construct the actual shift table by modifying the
    # above table.
    # Based upon pattern index upon mismatch with text
    # we want the shift along the text
    shift_table = []
    for i, p in enumerate(pattern):
        row = copy.copy(shift_dict)
        for mismatch in RADIX:
            if i < row[mismatch]:
                # righmost occurence of mismatch char in pattern
                # is farther right, so shift just 1
                row[mismatch] = 1
            else:
                # mismatch char is to the left of pattern index,
                # so we shift by appropriate difference.
                # Note this works if row[mismatch] is -1:
                # if mismatch char is not in the pattern,
                # we want to shift by one more than the number
                # of leftover chars in pattern
                row[mismatch] = i - row[mismatch]

        shift_table.append(row)

    return shift_table


def compare_text(pattern, text, idx, shift_table):
    shift = 0
    for i, tchar in enumerate(text):
        i = i + shift
        for j, pchar in reversed(enumerate(pattern)):
            if text[i+j] != pchar:
                shift += shift_table[j][text[i+j]]
                break
        

