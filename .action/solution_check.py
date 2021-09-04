#!/usr/bin/env python3
""" Check student's submission; requires the main file and the
    template file from the original repository. """

import os
import os.path
import logging
import sys
import subprocess
import pexpect
from logger import setup_logger
from parse_header import dict_header
from header_check import header_check
from srcutilities import compare_files, format_check, lint_check,\
glob_all_src_files

def identify(header):
    """ String to identify submission's owner. """
    ident = '(Malformed Header)'
    if header:
        ident = 'Grading {} {} {}'.format(header.get('name'),
            header.get('email'), header.get('github'))
    return ident

def build(file):
    """ Given a file, build with clang C++14 with Wall \
    and pedantic. Output is 'asgt'. It is left on the file system. """
    target = 'asgt'
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


def run(header, binary='asgt'):
    """ Run binary in a spawned shall via pexpect. """
    status = False
    if header:
        name = header.get('name').split(' ')[0]
        proc = pexpect.spawn('./' + binary)
        expect_list = [
            r'(.*[Hh]ello.*{}.*)'.format(name),
            r'(.*[Hh]ello.*)',
            pexpect.EOF,
        ]
        expect_match = proc.expect(expect_list)
        if expect_match < (len(expect_list) - 1):
            status = True
        else:
            logging.info('---- Failed ----')
            logging.info('Matched %s', proc.match)
            logging.info('Expected: "Hello %s!', name)
            logging.info('Received (last 100 chars):')
            logging.info(proc.before.decode('utf-8').rstrip('\r\n'))
    else:
        logging.info('Missing header, cannot run.')
    return status

def main():
    """ Main function for checking student's solution. """
    setup_logger()
    if len(sys.argv) < 3:
        logging.error('provide an input file and a base file.')
        sys.exit(1)
    with open(sys.argv[1]) as file_handle:
        contents = file_handle.read()
    header = dict_header(contents)
    logging.info('Start %s', identify(header))
    logging.info(os.getcwd())
    files = glob_all_src_files()
    logging.info('All files: %s', ' '.join(files))
    files_missing_header = [file for file in files \
        if not header_check(file)]
    if len(files_missing_header) != 0:
        logging.warning('Files missing headers: %s', ' '.join(files_missing_header))
    diff = compare_files(sys.argv[2], sys.argv[1])
    if len(diff) == 0:
        logging.error("No changes made from the base file. No grade.")
    else:
        if build(sys.argv[1]):
            logging.info('Build passed')
            if run(header):
                logging.info('Run passed')
                diff = format_check(sys.argv[1])
                if len(diff) != 0:
                    logging.warning("Error: Formatting needs improvement.")
                    logging.warning('\n'.join(diff))
                else:
                    logging.info('Formatting passed')
                lint_warnings = lint_check(sys.argv[1])
                if len(lint_warnings) != 0:
                    logging.warning('Error: Linter found improvements.')
                    logging.warning('\n'.join(lint_warnings))
                else:
                    logging.info('Linting passed')
            else:
                logging.error('Run failed')
        else:
            logging.error('Build failed')
    logging.info('End %s', identify(header))




if __name__ == '__main__':
    main()
