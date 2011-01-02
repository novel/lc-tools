"""Project-wise useful utils"""

import string

def int_sequence(sequence):
    """Function to transform integer suquences like '3-7,45,34-36' 
    and so forth to a list of integers, so for the sample sequence
    listed above it would be [3, 4, 5, 6, 7, 45, 34, 35, 36]

    @param sequence: sequence to be parsed
    @type sequence: str
    @return: list of integers
    @rtype: list
    """

    def _parse_token(token):
        syntax_description = "token syntax is: 'a-b'" \
            ", where a, b are integers, a > b"

        minus_sign_count = token.count("-")
        if minus_sign_count == 0:
            return [int(token)]
        elif minus_sign_count == 1:
            try:
                start, stop = token.split("-")
                if not start < stop:
                    raise ValueError
                return range(int(start), int(stop)+1)
            except ValueError:
                raise ValueError(syntax_description)
        else:
            raise ValueError(syntax_description)

    tokens = sequence.split(",")

    return sum(map(_parse_token, tokens), [])

def is_int_sequence(string_object):
    """Determine if the given string is an integer
    sequence as understood by L{I{int_sequence}
    function <int_sequence>}.

    @param string_object: string to check
    @type string_object: string
    @return: True if string_object is an int sequence,
        False otherwise
    @rtype: boolean"""

    return not len(set(string.ascii_letters) & set(string_object))
