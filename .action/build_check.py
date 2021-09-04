#!/usr/bin/env python3
""" Build the files given as arguments with a naive clang++ build. """
import os.path
import os
import sys
import logging
import subprocess
from logger import setup_logger

def build(file, target='asgt'):
    """ Given a file, build with clang C++14 with Wall \
    and pedantic. Output is 'asgt'. It is left on the file system. """
    if os.path.exists(target):
        os.unlink(target)
    # rm the file if exists
    status = True
    cmd = 'clang++ -Wall -pedantic -std=c++14 -o {} {}'.format(target, file)
    logging.debug(cmd)
    proc = subprocess.run([cmd], capture_output=True, shell=True, \
        timeout=10, check=False, text=True)
    if proc.stdout:
        logging.info('stdout: %s', str(proc.stdout).rstrip("\n\r"))
    if proc.stderr:
        logging.info('stderr: %s', str(proc.stderr).rstrip("\n\r"))
    if proc.returncode != 0:
        status = False
    return status

def main():
    """ Main function; process all files from the command line. """
    setup_logger()
    if len(sys.argv) < 2:
        logging.warning('Only %s arguments provided.', len(sys.argv))
    for in_file in sys.argv[1:]:
        logging.info('Building File: %s', in_file)
        if build(in_file):
            logging.info('Build passed.')
            logging.warning('Independently run and test your program'
                ' to ensure that it meets or exceeds all'
                ' requirements.')
            logging.warning('Full credit is assigned if and only if'
                ' the program meets or exceeds all requirements.')
        else:
            logging.error('Build failed. No credit will be assigned.')

if __name__ == '__main__':
    main()
