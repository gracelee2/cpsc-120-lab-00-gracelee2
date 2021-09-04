#!/usr/bin/env python3
""" Given a file and a keyword, fetch that value from the
    file's header. """

import sys

from parse_header import parse_header

def main():
    """ Main function, given a file and a keyword, fetch that value from the file's header. """
    if len(sys.argv) < 3:
        print("Not enough args. Exiting.")
        sys.exit(1)
    with open(sys.argv[1]) as file_handle:
        contents = file_handle.read()
    matches = parse_header(contents, sys.argv[2])
    if matches:
        print(matches)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
