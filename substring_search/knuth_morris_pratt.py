'''
Created on Jul 3, 2017

@author: suh
'''

# our alphabet consists of all printable ascii characters
from string import printable, ascii_lowercase

RADIX = ascii_lowercase


class DFA(object):
    ''' The Knuth--Morris--Pratt algorithm for substring search:

        The key idea is to create a lookup table based on the pattern,
        such that for any prefix of the pattern and for every possible
        next character in the input, we know what new prefix currently
        matches, i.e. is a suffix of the input processed so far.

        A clean way to implement this is as a discrete finite automaton
        (DFA), as in Sedgewick & Wayne's Algorithms.  Since every prefix
        of the pattern is determined by its length, we can simply use 
        the prefix length as the state of the DFA and we have to determine
        how an input character transitions the DFA to the next state.

        The state of the DFA ranges from 0 to N-1 where N is the length
        of the pattern string.  A state value of i while processing the
        input stream means the last i characters processed are maximal
        with respect to forming a prefix of the pattern.
    '''
    def __init__(self, pattern):
        self.pattern = pattern
        self.transition_table = self.preprocess_pattern(pattern)
        self.state = 0

    @classmethod
    def preprocess_pattern(cls, pattern):
        '''
        Uses Knuth--Morris--Pratt algorithm to preprocess lookup pattern
        into a prefix table, implemented as a discrete finite automaton.

        :param pattern: string to search for
        :returns: transition_table
        '''

        transition_table = []

        # first row is easy:
        # it has 0s for mismatches and a 1 for first char in pattern
        row = {}
        for char in RADIX:
            if char == pattern[0]:
                # on match, increase state value by 1
                row[char] = 1
            else:
                # on mismatch, stay in zero state
                row[char] = 0
        transition_table.append(row)

        aux_state = 0

        # start on 2nd letter of pattern
        for i, pattern_char in enumerate(pattern[1:], 1):
            row = {}
            for char in RADIX:
                if char == pattern_char:
                    # on match, increase state value by 1
                    row[char] = i + 1
                else:
                    # key insight: on mismatch, we can suppose the input stream
                    # starts on second letter of pattern and by induction, use
                    # a previous row of the transition table
                    row[char] = transition_table[aux_state][char]
            transition_table.append(row)
            # now we need to update our auxiliary state
            for char in RADIX:
                if char == pattern_char:
                    aux_state = transition_table[aux_state][char]

        return transition_table

    def read_char(self, char):
        ''' based on single character input and current state, transitions to next state '''
        self.state = self.transition_table[self.state][char]

    @property
    def found(self):
        ''' Returns boolean based on whether pattern has been matched '''
        return self.state == len(self.pattern)

    def read_stream(self, input_sequence):
        '''

        :param input_sequence: sequence of input characters, possibly infinite
        :returns: index of first match; index is length of sequence if no match
        '''
        for i, char in enumerate(input_sequence):
            self.read_char(char)
            print char, self.state
            if self.found:
                return i - len(self.pattern) + 1
        return i + 1


if __name__ == '__main__':
    pattern = 'fifofum'
    dfa = DFA(pattern)
    input_sequence = 'fififefofuhfeefififahlalafofumdumdumfeefifoofumfifkejfoolahlahfeefifeiiifeofeefifofumfieflfiefofuhfeefifif'
    ind = dfa.read_stream(input_sequence)

    if ind < len(input_sequence):
        print 'found pattern starting at index %s' % ind
    else:
        print 'did not find pattern'
