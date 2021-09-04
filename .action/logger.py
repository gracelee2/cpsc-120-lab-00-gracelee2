""" Local logger setup. Used across all the different bits and pieces
    in the GitHub actions. """

import logging
import sys

def setup_logger():
    """ Set up the logger to output to stdout. """
    # https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    #logging.basicConfig(filename='solution_check.log', encoding='utf-8', level=logging.INFO)
    # https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
