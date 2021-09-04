#!/usr/bin/env python3
""" Create a Clang compile commands DB named compile_commands.json
    which is used by the clang-tidy utility. """
import glob
import json
import os
from os.path import exists
import platform

def create_clang_compile_commands_db(remove_existing_db=False, \
    compile_cmd = 'clang++ -g -O3 -Wall -pipe -std=c++14'):
    """ Create a Clang compile commands DB named
        compile_commands.json in the current working directory."""
    out='compile_commands.json'
    linux_includes = ' -I/usr/include/c++/9/'
    darwin_includes = ' -D OSX -nostdinc++ -I/opt/local/include/libcxx/v1'
    my_platform = platform.system( )
    if my_platform == 'Linux':
        compile_cmd = compile_cmd + linux_includes
    elif my_platform == 'Darwin':
        compile_cmd = compile_cmd + darwin_includes
    compile_commands_db = [{'directory':'/tmp', 'command':'{} {}'.\
        format(compile_cmd, f), 'file':f} for f in glob.glob('*.cc')]
    if exists(out) and remove_existing_db:
        os.unlink(out)
    elif exists(out) and not remove_existing_db:
        print('Warning: the file "{}" already exists. Skipping.'.\
            format(out))
    else:
        with open(out, 'w') as file_handle:
            json.dump(compile_commands_db, file_handle)


if __name__ == '__main__':
    create_clang_compile_commands_db()
