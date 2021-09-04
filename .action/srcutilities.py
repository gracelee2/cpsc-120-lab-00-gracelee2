""" Utilities used to manipulate source code files from student
    assignments. """
import glob
import subprocess
import difflib
from mkcompiledb import create_clang_compile_commands_db

def remove_cpp_comments(file):
    """ Remove CPP comments from a file using the CPP preprocessor """
    # Inspired by
    # https://stackoverflow.com/questions/13061785/remove-multi-line-comments
    # and
    # https://stackoverflow.com/questions/35700193/how-to-find-a-search-term-in-source-code/35708616#35708616
    no_comments = None
    cmd = 'clang++ -E -P -'
    with open(file) as file_handle:
        # replace 'a', '__' and '#' to avoid preprocessor handling
        filtered_contents = file_handle.read().replace('a', 'aA').\
        replace('__', 'aB').replace('#', 'aC')
    proc = subprocess.run([cmd], capture_output=True, shell=True, \
        timeout=10, check=False, text=True, input=filtered_contents)
    if proc.returncode == 0:
        no_comments = proc.stdout.replace('aC', '#').replace('aB', '__').replace('aA', 'a')
    else:
        print('Errors encountered removing comments.')
        print('stderr {}'.format(str(proc.stderr).rstrip("\n\r")))
    return no_comments

def compare_files(base_file, submission_file):
    """ Compare two source files with a contextual diff, return \
    result as a list of lines. """
    base_file_contents_no_comments = remove_cpp_comments(base_file).split('\n')
    contents_no_comments = remove_cpp_comments(submission_file).\
        split('\n')
    diff = difflib.context_diff(base_file_contents_no_comments, \
        contents_no_comments, 'Base', 'Submission', n=3)
    return list(diff)

def format_check(file):
    """ Use clang-format to check file's format against the \
    Google C++ style. """
    # clang-format
    cmd = 'clang-format'
    cmd_options = '-style=Google --Werror'
    cmd = cmd + ' ' + cmd_options + ' ' + file
    proc = subprocess.run([cmd], capture_output=True, shell=True, \
        timeout=10, check=False, text=True)
    correct_format = str(proc.stdout).split('\n')
    with open(file) as file_handle:
        original_format = file_handle.read().split('\n')
    diff = difflib.context_diff(original_format, correct_format, \
        'Student Submission', 'Correct Format', n=3)
    #print('\n'.join(list(diff)))
    return list(diff)


def lint_check(file):
    """ Use clang-tidy to lint the file. Options for clang-tidy \
    defined in the function. """
    # clang-tidy
    create_clang_compile_commands_db(remove_existing_db=True)
    cmd = 'clang-tidy'
    cmd_options = r'-checks="-*,google-*, modernize-*, \
    readability-*,cppcoreguidelines-*,\
    -google-build-using-namespace,\
    -modernize-use-trailing-return-type,\
    -cppcoreguidelines-avoid-magic-numbers,\
    -readability-magic-numbers,\
    -cppcoreguidelines-pro-type-union-access,\
    -cppcoreguidelines-pro-bounds-constant-array-index"'
    #cmd_options = '-checks="*"'
    cmd = cmd + ' ' + cmd_options + ' ' + file
    proc = subprocess.run([cmd], capture_output=True, shell=True, \
        timeout=10, check=False, text=True)
    linter_warnings = str(proc.stdout).split('\n')
    linter_warnings = [line for line in linter_warnings if line != '']
    return linter_warnings

def glob_all_src_files():
    """ Recurse through the CWD and find all the .cc and .h files. """
    files = glob.glob('*.cc', recursive=True) + glob.glob('*.h', recursive=True)
    return files
