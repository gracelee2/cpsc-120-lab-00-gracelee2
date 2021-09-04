#!/usr/bin/env python3
""" Run the files given as arguments with the provided arguments. """

import os.path
import os
import sys
import logging
import subprocess
from logger import setup_logger

def run(binary='asgt', args='', expect=None):
    """ Run binary in a spawned. This run does not test. """
    status = True
    cmd = './' + binary
    if os.path.exists(cmd):
        if len(args) > 0:
            cmd = cmd + ' ' + args
        proc = subprocess.run([cmd], capture_output=True, shell=True, \
            timeout=10, check=False, text=True)
        if proc.stdout:
            logging.info('Output (stdout): %s', str(proc.stdout).rstrip("\n\r"))
            if expect:
                logging.info('Expected: %s', expect)
        if proc.stderr:
            logging.warning('Errors (stderr): %s', str(proc.stderr).rstrip("\n\r"))
        if proc.returncode != 0:
            status = False
    else:
        logging.warning('The binary %s does not exist.', cmd)
        status = False
    return status


def main():
    """ Main function; process the given binary and included
        command line options. """
    setup_logger()
    if len(sys.argv) < 2:
        logging.warning('Only %s arguments provided.', len(sys.argv))
    cmd = sys.argv[1]
    cmd_args = ""
    if len(sys.argv) > 2:
        cmd_args = " ".join(sys.argv[2:])
    logging.warning('This is not an exhaustive test or a grader. The'
        ' program shall be executed to verify that it does not crash.'
        ' Students are required to develop their own testing regimen.')
    if len(cmd_args) > 0:
        logging.info('Executing: "%s %s"', cmd, cmd_args)
    else:
        logging.info('Executing: "%s"', cmd)
    if run(cmd, cmd_args, 'Hello your-name!'):
        logging.info('Your program executed and exited cleanly.'
            ' Perform further testing to ensure that your program'
            ' meets or exceeds all requirements.')
    else:
        logging.warning('Your program did not execute cleanly.')

if __name__ == '__main__':
    main()
