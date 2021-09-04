#!/usr/bin/env python3
""" Given a file, verify if the file has a header.
 Example C++ header
// Michael Shafae
// CPSC 120-01
// 2021-01-30
// mshafae@csu.fullerton.edu
// @mshafae
//
// Lab 00-00
//
// This is my first program and it prints out Hello World!
//
"""

import sys
import logging
from logger import setup_logger
from header_check import header_check

def main():
    """ Main function; process each file given through
        header_check. """
    setup_logger()
    if len(sys.argv) < 2:
        logging.warning('Only %s arguments provided.', len(sys.argv))
    status = 0
    for in_file in sys.argv[1:]:
        logging.debug('Check header for file: %s', in_file)
        if not header_check(in_file):
            logging.warning('Header is malformed or missing.')
            status = 1
        else:
            logging.debug('Header found.')
    sys.exit(status)

if __name__ == '__main__':
    main()
