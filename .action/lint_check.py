#!/usr/bin/env python3
""" Check the given files to see if they conform to good programming
    practices using clang-tidy. """

import sys
import logging
from logger import setup_logger
from srcutilities import lint_check

def main():
    """ Main function; process each file given through clang-tidy. """
    setup_logger()
    status = 0
    if len(sys.argv) < 2:
        logging.warning('Only %s arguments provided.', len(sys.argv))
    for in_file in sys.argv[1:]:
        logging.info('Linting file: %s', in_file)
        lint_warnings = lint_check(in_file)
        if len(lint_warnings) != 0:
            logging.warning('Error: Linter found improvements.')
            logging.warning('\n'.join(lint_warnings))
            status = 1
        else:
            logging.info('Linting passed')
    sys.exit(status)


if __name__ == '__main__':
    main()
