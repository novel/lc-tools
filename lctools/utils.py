def int_sequence(str):
    """Function to transform integer suquences like '3-7,45,34-36' 
    and so forth to a list of integers, so for the sample sequence
    listed above it would be [3, 4, 5, 6, 7, 45, 34, 35, 36]"""

    def _parse_token(token):
        syntax_description = "token syntax is: 'a-b'" \
            ", where a, b are integers, a > b"

        minus_sign_count = token.count("-")
        if minus_sign_count == 0:
            return int(token)
        elif minus_sign_count == 1:
            try:
                start, stop = token.split("-")
                if not start < stop:
                    raise ValueError
                return range(start, stop+1)
            except ValueError:
                raise ValueError(syntax_description)
        else:
            raise ValueError(syntax_description)

    tokens = str.split(",")

    return sum(map(_parse_token, tokens), [])
