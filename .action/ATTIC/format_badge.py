#!/usr/bin/env python3
""" Check the given files to see if they conform to the Google C++
    Programming style using clang-format. """

import sys
import logging
from logger import setup_logger
from srcutilities import format_check

def main():
    """ Main function; check the format of each file on the
    command line. """
    setup_logger()
    if len(sys.argv) < 2:
        logging.warning('Only %s arguments provided.', len(sys.argv))
    status = 0
    for in_file in sys.argv[1:]:
        logging.debug('Checking format for file: %s', in_file)
        diff = format_check(in_file)
        if len(diff) != 0:
            logging.warning("Error: Formatting needs improvement.")
            status = 1
        else:
            logging.debug('Formatting passed')
    sys.exit(status)

if __name__ == '__main__':
    main()
