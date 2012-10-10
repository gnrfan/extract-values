"""
A Python module for extracting values out of a string using a simple pattern
of named group of characters delimited by a pair of opening and closing
delimiters as a simpler alternative to using regular expressions.

E.g.
>>> from extract_values import extract_values
>>> extract_values('John Doe <john@example.com> (http://example.com)', \
'{name} <{email}> ({url})')
{'url': 'http://example.com', 'name': 'John Doe', 'email': 'john@example.com'}
"""
import re

__version__ = '1.0'


class error(Exception):
    pass


def extract_values(
    string, pattern, lowercase=False, whitespace=None,
    strip_values=False, delimiters=['{', '}']
):
    """
    Extracts values from a string using a pattern made of named groups
    of characters.

    Optional parameters:

    lowercase - When True is passed the string is lowercased first
    whitespace - Minimal number of extra whitespace to remove
    strip_values - When True calls strip() for each value removing whitespace
    delimiters - A sequence with only the opening and closing delimiters
    """
    # Checking for lowercase convertion
    if lowercase:
        string = string.lower()

    # Checking for a sequence in delimiters
    try:
        delimiters = tuple(delimiters)
    except TypeError, e:
        raise error('Error with delimiters since %s' % e)

    # Checking for just two delimiters
    if len(delimiters) != 2:
        raise error('delimiters must be a sequence with just two characters')

    # Check if whitespace should be removed
    whitespace_error_message = (
        'whitespace must be a non-negative integer '
        'with the minimal number of continous whitespace '
        'to remove'
    )

    if whitespace is not None:
        # Make sure it's an integer
        try:
            whitespace = int(whitespace)
        except TypeError:
            raise error(whitespace_error_message)

        # Make sure it's a non-negative integer
        if whitespace < 0:
            raise error(whitespace_error_message)

        # Now remove whitespace
        if whitespace == 0:
            # Removing all whitespace from each value
            string = re.sub('\s',  '', string)
        else:
            # Removing only extra whitespace from each value
            string = re.sub(
                '(\s)\s{%d,}' % (whitespace - 1), '\\1', string
            )

    # Helper regular expressions
    splitter = re.compile('(%s\w+%s)' % (delimiters[0], delimiters[1]))
    extracter = re.compile('%s(\w+)%s' % (delimiters[0], delimiters[1]))

    # Split pattern into parts including named groups
    parts = splitter.split(pattern)

    # Expand group or escape non-group
    for idx, p in enumerate(parts):
        # Part is a named group
        if splitter.match(p):
            name = extracter.search(p).groups()[0]
            parts[idx] = '(?P<%s>.+)' % name
        # Part is something else
        else:
            # Escape values with special semantics in regular expressions
            parts[idx] = re.escape(p)

    # Build expanded pattern
    expanded_pattern = '^%s$' % ''.join(parts)

    try:
        # Attempt to extract values
        value_dict = re.match(expanded_pattern, string).groupdict()

        # Check if values must be stripped
        if strip_values:
            for name in value_dict:
                value_dict[name] = value_dict[name].strip()

        # Finally, return values
        return value_dict

    except re.error, e:
        # Something went wrong, we pass along the message from re module
        raise error(e.message)

    except AttributeError:
        # No regexp match, just return an empty dictionary
        return {}
