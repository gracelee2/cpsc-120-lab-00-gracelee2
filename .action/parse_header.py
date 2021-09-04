""" Parses the header define by the example given below. """
# Example C++ header
#// Michael Shafae
#// CPSC 120-01
#// 2021-01-30
#// mshafae@csu.fullerton.edu
#// @mshafae
#//
#// Lab 00-00
#//
#// This is my first program and it prints out Hello World!
#//

import re

HEADER_REGEX = r"(#|/{2}) ([a-zA-Z0-9_-]+) ([a-zA-Z0-9_-]+)\n(#|/{2}) ([a-zA-Z]{4} \d\d\d-\d\d)\n(#|/{2}) \d\d\d\d-\d\d?-\d\d?\n(#|/{2}) (\w+[.-_0-9\w]*@csu\.fullerton\.edu)\n(#|/{2}) @([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38})\n(#|/{2})\s*\n(#|/{2}) (Lab \d\d-\d\d)\n(#|/{2})\s*\n(#|/{2}) (\w+.*)\n(#|/{2})"

def parse_header(contents, keyword=None):
    """ Given Given a single string, parse the header and return the keyword's value. """
    header_re = re.compile(HEADER_REGEX)
    matches = re.findall(header_re, contents)
    value = None
    header_matches = None
    if len(matches) >= 1:
        header_matches = matches[0]
    if header_matches:
        if keyword == 'name':
            value = '"{} {}"'.format(matches[1], matches[2])
        elif keyword == 'class':
            value = matches[4]
        elif keyword == 'email':
            value = matches[7]
        elif keyword == 'github':
            value = matches[9]
        elif keyword == 'asgt':
            value = matches[12]
        elif keyword == 'comment':
            value = matches[15]
        elif keyword is None:
            value = header_matches
    return value

def dict_header(contents):
    """ Given a single string, parse the header and return the result
        as a dictionary with the keys class, email, github, asgt, comment. """
    header_re = re.compile(HEADER_REGEX)
    matches = re.findall(header_re, contents)
    header_d = None
    if len(matches) >= 1:
        matches = matches[0]
        header_d = {'name': '{} {}'.format(matches[1], matches[2]),
            'class': matches[4],
            'email': matches[7],
            'github': matches[9],
            'asgt': matches[12],
            'comment': matches[15],}
    return header_d
